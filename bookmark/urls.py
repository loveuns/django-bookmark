from django.urls import path
from .views import BookmarkLV, BookmarkDetailV, BookmarkUV, BookmarkDeleteV, BookmarkCV

app_name = 'bookmark'
urlpatterns = [
    # /
    # /5/detail/
    # /5/update/
    # /5/delete/
    # /add/

    path('',                 BookmarkLV.as_view(),       name='list'),
    path('<int:pk>/detail/', BookmarkDetailV.as_view(),  name='detail'),
    path('<int:pk>/update/', BookmarkUV.as_view(),       name='update'),
    path('<int:pk>/delete/', BookmarkDeleteV.as_view(),  name='delete'),
    path('add/',             BookmarkCV.as_view(),       name='create'),
]
