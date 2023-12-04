from django.urls import path 

from apps.posts.views import PostAPIView

urlpatterns = [
    path('', PostAPIView.as_view(), name="api_posts")
]