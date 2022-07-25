from django.urls import path, re_path

from . import views 

#app_name = 'music'
urlpatterns = [
    re_path(r'^$', views.IndexView.as_view(), name='index'),
    re_path(r'^register/$', views.UserFormView.as_view(), name='register'),
    re_path(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    #music/album/add
    re_path(r'album/add/$', views.AlbumCreate.as_view(), name='album-add'),
]
