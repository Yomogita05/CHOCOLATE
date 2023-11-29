from typing import Any
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render

from django.views.generic.base import TemplateView

from django.contrib import messages

from django.core.mail import EmailMessage

from django.views.generic import ListView,CreateView,FormView

from django.urls import reverse_lazy

from .forms import Channel1Form,Channel2Form,Channel3Form,ContactForm

from django.utils.decorators import method_decorator

from django.contrib.auth.decorators import login_required
# モデルWebsystemをインポート
from .models import Channel1_data,Channel2_data,Channel3_data



class IndexView(TemplateView):
    # index.htmlをレンダリングする
    template_name = "index.html"

class TalkView(TemplateView):
    # talk.htmlをレンダリングする
    template_name = "talk.html"

class Channel1View(ListView):
    # channel1.htmlをレンダリングする
    template_name = "channel1.html"
    # object_listキー名の別名を設定
    context_object_name = "Channel1_records"

    queryset = Channel1_data.objects.order_by("posted_at")

    # 1ページに表示するレコードの件数
    paginate_by = 100

class Channel2View(ListView):
    # channel2.htmlをレンダリングする
    template_name = "channel2.html"
    # object_listキー名の別名を設定
    context_object_name = "Channel2_records"

    queryset = Channel2_data.objects.order_by("posted_at")

    # 1ページに表示するレコードの件数
    paginate_by = 100

class Channel3View(ListView):
        # channel3.htmlをレンダリングする
    template_name = "channel3.html"
    # object_listキー名の別名を設定
    context_object_name = "Channel3_records"

    queryset = Channel3_data.objects.order_by("posted_at")

    # 1ページに表示するレコードの件数
    paginate_by = 100

@method_decorator(login_required,name="dispatch")
class CreateViewC1(CreateView):
        form_class = Channel1Form
        template_name = "channel1form.html"
        success_url = reverse_lazy("websystem:channel1")

        def get_initial(self):
             initial = super().get_initial()
             initial["name"] = "本当にあった怖い匿名"
             return initial
        
        def form_valid(self,form):
            postdata = form.save(commit=False)
            postdata.save()
            return super().form_valid(form)

@method_decorator(login_required,name="dispatch")
class CreateViewC2(CreateView):
        form_class = Channel2Form
        template_name = "channel2form.html"
        success_url = reverse_lazy("websystem:channel2")

        def get_initial(self):
             initial = super().get_initial()
             initial["name"] = "世にも奇妙な匿名"
             return initial

        def form_valid(self,form):
            postdata = form.save(commit=False)
            postdata.save()
            return super().form_valid(form)

@method_decorator(login_required,name="dispatch")
class CreateViewC3(CreateView):
        form_class = Channel3Form
        template_name = "channel3form.html"
        success_url = reverse_lazy("websystem:channel3")

        def get_initial(self):
             initial = super().get_initial()
             initial["name"] = "匿名さん"
             return initial

        def form_valid(self,form):
            postdata = form.save(commit=False)
            postdata.save()
            return super().form_valid(form)

class ContactView(FormView):
    """問い合わせページを表示するビュー

    フォームで入力されたデータを取得し、メールの作成と送信を行う
    """
    # contact.htmlをレンダリングする
    template_name = "contact.html"
    # クラス変数form_classにforms.pyで定義したContactFormを設定
    form_class = ContactForm
    # 送信完了後にリダイレクトするページ
    success_url = reverse_lazy("websystem:contact")

    def form_valid(self,form):
        """FormViewクラスのform_vaild()をオーバーライド
        フォームバリエーションを通過したデータがPostされた時に呼ばれる
        メール送信を行う

        parameters:
            form(object): ContactFormのオブジェクト
        Return:
            HttpResponseRedirectのオブジェクト
            オブジェクトをインスタンス化するとsuccess_urlで
            設定されているURLにリダイレクトされる
        """
        # return HttpResponseRedirect(self.get_success_url)

        # フォームに入力されたデータをフィールド名を指定して取得
        name = form.cleaned_data["name"]
        email = form.cleaned_data["email"]
        title = form.cleaned_data["title"]
        message = form.cleaned_data["message"]
        # メールのタイトルの書式の設定
        subject = "お問い合わせ:{}".format(title)
        # フォームの入力データの書式を設定
        message = \
            "送信者名:{0}\nメールアドレス:{1}\nタイトル:{2}\nメッセージ:{3}"\
            .format(name,email,title,message)

        # メールの送信元のアドレス
        from_email = "utm2377066@outlook.com"
        # 送信先のアドレス
        to_list = ["utm2377066@outlook.com"]
        # EmailMessageオブジェクトを生成
        message = EmailMessage(subject=subject,
                               body=message,
                               from_email=from_email,
                               to=to_list,
                               )
        # EmailMessageクラスのsend()でメールサーバからメールを送信
        message.send()
        # 送信完了後に表示するメッセージ
        messages.success(
            self.request,"お問い合わせは正常に送信されました。")
        # 戻り値はスーパークラスのform_valid()戻り値(HttpResponseRedirect)
        return super().form_valid(form)
 