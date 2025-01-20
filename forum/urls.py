from django.urls import path
from . import views

urlpatterns = [
    path('', views.forum_post_list, name='forum_post_list'),
    path('add_post/', views.add_post, name='add_post'),       # Add post view
    path('<slug:slug>/', views.forum_post_detail, name='forum_post_detail'),  # Detail view
    path('<slug:slug>/edit/', views.edit_post, name='edit_post'),  # Edit post view
    path('<slug:slug>/delete/', views.delete_post, name='delete_post'),  # Delete post view
    path('<slug:slug>/add_comment/', views.add_comment, name='add_comment'), # Add comment to post
    path('comment/<int:comment_id>/edit/', views.edit_comment, name='edit_comment'), # Edit comment
    path('comment/<int:comment_id>/delete/', views.delete_comment, name='delete_comment'), # Delete comment
]
