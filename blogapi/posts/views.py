from rest_framework import generics, permissions 
from .models import Post
from .permissions import IsAuthorOrReadOnly
from .serializers import PostSerializer

class PostList(generics.ListCreateAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    permission_classes = (permissions.IsAdminUser,) 
    queryset = Post.objects.all()
    serializer_class = PostSerializer
