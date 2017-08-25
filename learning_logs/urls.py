"""Define urlpatterns of 'learning_logs'."""

from django.conf.urls import url

from . import views

urlpatterns=[
    # main page
    url(r'^$', views.index, name='index'),

    # show all topics
    url(r'^topics/$', views.topics, name='topics'),

    # show single topic and all of it's entries.
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),

    # page for adding new topic
    url(r'^new_topic/$', views.new_topic, name='new_topic')
]
