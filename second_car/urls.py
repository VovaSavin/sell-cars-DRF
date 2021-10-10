from django.urls import path

from . import views

urlpatterns = [
    path("type-body/", views.ListCategoryView.as_view()),
    path("type-body/<str:slug>/", views.DetailCategoryView.as_view()),
    path("adverts/", views.ListCarAdvertApi.as_view()),
    path("adverts/<int:pk>/", views.DetailCarAdvertApi.as_view()),
    path("create-adverts/", views.CreateAdvertView.as_view()),
]
