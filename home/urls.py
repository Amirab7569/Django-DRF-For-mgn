from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view() ,name='home' ),
    path('question/', views.QuestionListView.as_view() ),
    path('question/create/', views.QuestionCreateView.as_view()),
    path('question/update/<int:pk>/', views.QuestionUpddateView.as_view()),
    path('question/delete/<int:pk>/', views.QuestionDeleteView.as_view()),
    
]
