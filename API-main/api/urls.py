from django.urls import path
from.import views

urlpatterns=[
    path("", views.Getdata),
    path("add-item/", views.addItem),
]