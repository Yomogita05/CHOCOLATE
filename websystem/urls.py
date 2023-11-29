from django.urls import path
from .import views


app_name = "websystem"

urlpatterns = [
    path("",views.IndexView.as_view(), name="index"),

    path("talk",views.TalkView.as_view(), name="talk"),
    
    path("channel1",views.Channel1View.as_view(), name="channel1"),
    
    path("channel2",views.Channel2View.as_view(), name="channel2"),

    path("channel3",views.Channel3View.as_view(), name="channel3"),

    path("channel1form",views.CreateViewC1.as_view(),name="channel1form"),

    path("channel2form",views.CreateViewC2.as_view(),name="channel2form"),

    path("channel3form",views.CreateViewC3.as_view(),name="channel3form"),

    path("contact",views.ContactView.as_view(),name="contact"),
]