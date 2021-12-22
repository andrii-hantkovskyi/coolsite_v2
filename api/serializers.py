from rest_framework.serializers import ModelSerializer

from main.models import GameCategory, Game, Post


class GameCategorySerializer(ModelSerializer):
    class Meta:
        model = GameCategory
        fields = '__all__'


class GameSerializer(ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'

    def to_representation(self, instance):
        rep = super(GameSerializer, self).to_representation(instance)
        rep['category'] = GameCategorySerializer(instance.category).data
        return rep


class PostSerializer(ModelSerializer):

    class Meta:
        model = Post
        fields = ('game', 'title', 'content')

    def to_representation(self, instance):
        rep = super(PostSerializer, self).to_representation(instance)
        rep['game'] = GameSerializer(instance.game).data
        return rep
