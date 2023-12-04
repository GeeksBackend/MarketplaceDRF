from rest_framework.generics import ListAPIView

from apps.posts.models import Post
from apps.posts.serializers import PostSerializer

# Create your views here.
class PostAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer