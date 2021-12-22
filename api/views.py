# Create your views here.
from rest_framework.viewsets import ModelViewSet

from api.serializers import GameCategorySerializer, GameSerializer, PostSerializer
from main.models import GameCategory, Game, Post


class GameCategoryViewSet(ModelViewSet):
    serializer_class = GameCategorySerializer
    queryset = GameCategory.objects.all()


class GameViewSet(ModelViewSet):
    serializer_class = GameSerializer
    queryset = Game.objects.all()


class PostViewSet(ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.filter(in_archive=False)
