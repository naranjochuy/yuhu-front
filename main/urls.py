from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views

urlpatterns = [
    path("", login_required(views.list), name="list"),
    path("create", login_required(views.create), name="create"),
    path("update/<int:id>/", login_required(views.update), name="update"),
    path("delete/<int:id>/", login_required(views.delete), name="delete"),
]
