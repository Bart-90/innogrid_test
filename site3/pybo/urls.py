from django.urls import path
from . import views

app_name = 'pybo'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:world_id>', views.detail, name='detail'),
    path('reserv/<int:world_id>', views.reservation, name='reservation'),
    path('question/', views.index1, name='index1'),
    path('notification/', views.notification, name='notification'),
    path('QnA/', views.QnA, name='QnA'),    
    path('question/<int:question_id>', views.detail1, name='detail1'),
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
    path('question/create/', views.question_create, name='question_create'),
]