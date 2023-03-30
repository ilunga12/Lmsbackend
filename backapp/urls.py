from django.urls import path

from backapp import views

urlpatterns = [
    path('teachers/', views.Teacher_List.as_view()),
    path('teachers/<int:pk>/', views.Teacher_Detail.as_view()),
]
