from rest_framework.routers import DefaultRouter

from django.urls import include, path

from rest_framework.authtoken import views
from .views import PostViewSet, GroupViewSet, CommentViewSet

app_name = 'api'

router = DefaultRouter()

router.register(r'posts', PostViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet,
                basename='comment')

urlpatterns = [
    path('api-token-auth/', views.obtain_auth_token),
    path('', include(router.urls))
]
