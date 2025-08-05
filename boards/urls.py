from django.urls import path

from . import views

urlpatterns = [
    path("/api/boards/", views.board_list, name="board_list"),
]