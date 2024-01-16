from django.urls import path
from . import views

urlpatterns = [
      path('user/create/', views.CreateUser.as_view(), name='create-user'),
      path('user/login/', views.LoginUserView.as_view(), name='login-user'),
      path('user/<int:pk>/', views.RetrieveUser.as_view(), name='get-user'),
      path('user/update/', views.UpdateUser.as_view(), name='update-user'),
      path('user/delete/<int:pk>/', views.DestroyUser.as_view(), name='delete-user'),
      
      
      
      path('posts/', views.RetrieveUserPosts.as_view(), name='all-posts'),
      path('post/create/', views.CreatePost.as_view(), name='create-post'),
      path('post/<int:pk>/', views.RetrievePost.as_view(), name='view-post'),
      path('post/update/<int:pk>/', views.UpdatePost.as_view(), name='edit-post'),
      path('post/delete/<int:pk>/', views.DestroyPost.as_view(), name='delete-post'),
      
      
      
      path('post/like/<int:pk>/', views.LikePost.as_view(), name='like-post'),


      path('post/comment/<int:pk>/', views.CommentPost.as_view(), name='comment-on-post'),
      path('post/comments/<int:pk>/', views.CommentPost.as_view(), name='view-comment-post'),
  
  
      path('user/follow/<int:pk>/', views.FollowUser.as_view(), name='follow-user'),
      
]