from django.urls import path, include
from .views import *

urlpatterns = [
    path('', ApiRoot.as_view(), name=ApiRoot.name),

    path('import/', ImportJson.as_view(), name=ImportJson.name),

    path('users/', UserList.as_view(), name=UserList.name),
    path('users/<int:pk>/', UserDetail.as_view(), name=UserDetail.name),

    path('profiles/', ProfileList.as_view(), name=ProfileList.name),
    path('profiles/<int:pk>/', ProfileDetail.as_view()),

    path('profile-posts/', ProfilePostList.as_view(), name=ProfilePostList.name),
    path('profile-posts/<int:pk>/', ProfilePostDetail.as_view(), name=ProfilePostDetail.name),

    path('posts-comments/', PostCommentList.as_view(), name=PostCommentList.name),
    path('posts-comments/<int:pk>/', PostCommentDetail.as_view(), name=PostCommentDetail.name),

    path('posts/<int:pk>/comments/', CommentList.as_view(), name=CommentList.name),
    path('posts/<int:post_pk>/comments/<int:comment_pk>/', CommentDetail.as_view(), name=CommentDetail.name),

    path('profile-posts-comments/', ProfilePostsComments.as_view(), name=ProfilePostsComments.name),

    path('api-auth/', include('rest_framework.urls'))
] 
