from rest_framework import generics
from .models import Link as Links
from .serizliers import LinkSerializer

# Create your views here.
class PostListApi(generics.ListAPIView):
    queryset = Links.objects.filter(active=True)

    serializer_class = LinkSerializer
class PostCreateApi(generics.CreateAPIView):
    queryset = Links.objects.filter(active=True)

    serializer_class = LinkSerializer

class PostDetailApi(generics.RetrieveAPIView):
    queryset = Links.objects.filter(active=True)

    serializer_class = LinkSerializer
class PostUpdateApi(generics.UpdateAPIView):
    queryset = Links.object.filter(active=True)

    serializer_class = LinkSerializer
class PostDeleteApi(generics.DestroyAPIView):
    queryset= Links.objects.filter(active=True)

    serializer_class = LinkSerializer

