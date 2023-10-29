from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path("", views.index, name = "index" ),
    path("add_data", views.add_data, name = "add_data" ),
    path("showpage/", views.show_data, name = "show_page"),
    path("editpage/<int:pk>", views.edit_page, name = "edit_page"),
    path("update/<int:pk>", views.Updatedata, name = "Updatedata"),
    path("delete/<int:pk>", views.deletedata, name = "deletedata"),
]