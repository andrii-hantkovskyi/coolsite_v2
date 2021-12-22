from rest_framework.routers import SimpleRouter

from api.views import GameCategoryViewSet, PostViewSet, GameViewSet

router = SimpleRouter()

urlpatterns = []

router.register('game-categories', GameCategoryViewSet, basename='game categories')
router.register('games', GameViewSet, basename='games')
router.register('posts', PostViewSet, basename='posts')

urlpatterns += router.urls
