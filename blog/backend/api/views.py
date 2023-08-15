from rest_framework import generics, permissions

from posts.models import Post
from .serializers import PostSerializer

from .permissions import IsAuthorOrReadOnly


class PostList(generics.ListCreateAPIView):
    # permission_classes = (permissions.IsAuthenticated,) # OOB view-level permission
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (permissions.IsAuthenticated,) # OOB view-level permission

    permission_classes = (
        IsAuthorOrReadOnly,
    )  # custom view-level, object-level permission
    queryset = Post.objects.all()
    serializer_class = PostSerializer
