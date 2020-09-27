from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('topics/', views.topics, name='topics_link'),
    path('topics/<int:topic_id>/', views.topic, name='individual_topic'),
    path('new_topic', views.new_topic, name='new_topic'),
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry')
]