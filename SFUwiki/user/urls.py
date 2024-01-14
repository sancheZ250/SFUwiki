from django.urls import path, include, re_path

from user.views import IsModeratorAPI

urlpatterns = [
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    path('api/v1/is_moder/', IsModeratorAPI.as_view())
]

# /api/v1/drf-auth/login/ - POST с username и password, логиним пользователя
# /auth/token/login/ - получение токена(POST запрос с username и password)
# /api/v1/auth/users/ - регистрация пользователя (POST), получение списка пользователей (GET)
# /auth/token/logout/ - выход из системы, удаление токена (POST-запрос, токен в заголовке)
