from django.urls import path
from .views import *


urlpatterns = [
    path('', main, name='main'),
    path('history-baidybek',historyBaidybekView,name="historyBaidybek"),
    path('shayan',shayanView,name="shayan"),
    path('borlisay',borlisayView,name="borlisay"),
    path('cat/<slug:slug>', category_detailView, name='category_detailView'),
    path('media-cat/<slug:slug>', mediaCategory_detailView, name='mediaCategory_detailView'),
    path('posts/<slug:slug>', postDetailView, name='post'),
    path('media-posts/<slug:slug>', mediaPostDetailView, name='media_post'),

]