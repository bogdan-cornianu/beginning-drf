from django.conf.urls import include, url
from django.contrib import admin
from todo import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    # Todos endpoints
    url(r'^api/v1/todos/$', views.TodosView.as_view()),
    url(r'^api/v1/todos/(?P<todo_id>[0-9]*)$', views.TodosView.as_view()),
]
