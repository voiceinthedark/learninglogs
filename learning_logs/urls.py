"""Define Urls patterns for learning_logs"""

from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Home page
    url(r'^$', views.index, name='index'),
    # show all topics
    path('topics/', views.topics, name='topics'),
    # detail page for a single topic
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    path('topics/new_topic', views.new_topic, name='new_topic'),
]
