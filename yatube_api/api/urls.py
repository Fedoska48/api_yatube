from rest_framework.routers import DefaultRouter

from django.urls import include, path

from .views import PostViewSet, GroupViewSet, CommentViewSet

app_name = 'api'

router = DefaultRouter()

router.register('posts', PostViewSet)
router.register('groups', GroupViewSet)
router.register('comments', CommentViewSet)

urlpatterns = [
    path('api-token-auth/', include(router.urls)),
    path('posts/', include(router.urls)),
    path('posts/{post_id}/', include(router.urls)),
    path('groups/', include(router.urls)),
    path('groups/{group_id}/', include(router.urls)),
    path('posts/{post_id}/comments/', include(router.urls)),
    path('posts/{post_id}/comments/{comment_id}/', include(router.urls))
]

# api/v1/api-token-auth/ (POST): передаём логин и пароль, получаем токен.
# api/v1/posts/ (GET, POST): получаем список всех постов или создаём новый пост.
# api/v1/posts/{post_id}/ (GET, PUT, PATCH, DELETE): получаем, редактируем или удаляем пост по id.
# api/v1/groups/ (GET): получаем список всех групп.
# api/v1/groups/{group_id}/ (GET): получаем информацию о группе по id.
# api/v1/posts/{post_id}/comments/ (GET, POST): получаем список всех комментариев поста с id=post_id или создаём новый, указав id поста, который хотим прокомментировать.
# api/v1/posts/{post_id}/comments/{comment_id}/ (GET, PUT, PATCH, DELETE): получаем, редактируем или удаляем комментарий по id у поста с id=post_id.