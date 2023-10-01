from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter
from rest_framework_nested import routers
from .views import index, InstituteViewSet, DepartmentViewSet, TeacherViewSet, DisciplineViewSet, TeacherReviewViewSet

router = DefaultRouter()
router.register(r'institutes', InstituteViewSet)

institute_router = routers.NestedSimpleRouter(router, r'institutes')
institute_router.register(r'departments', DepartmentViewSet, basename='institute_departments')
institute_router.register(r'teachers', TeacherViewSet, basename='institute-teachers')

router.register(r'disciplines', DisciplineViewSet)

institute_router.register(r'teachers/(?P<teacher_id>[^/.]+)/reviews', TeacherReviewViewSet, basename='teacher_reviews')
urlpatterns = [
    path('', index),
    path('api/v1/', include(router.urls)),
    path('api/v1/', include(institute_router.urls)),
]


# api/v1/institutes/ - список институтов.
# api/v1/institutes/<institute_id>/ - информация о конкретном институте.
# api/v1/institutes/<institute_id>/departments/ - список кафедр в институте.
# api/v1/institutes/<institute_id>/departments/<department_id>/ - информация о конкретной кафедре.
# api/v1/institutes/<institute_id>/teachers/ - список преподавателей в институте.
# api/v1/institutes/<institute_id>/teachers/<teacher_id>/ - информация о конкретном преподавателе.
# api/v1/disciplines/ - список дисциплин
# api/v1/disciplines/<discipline_id>/ - Информация о конкретной дисциплине
# /api/v1/institutes/<institute_id>/teachers/<teacher_id>/reviews/ - Информация о отзывах на преподавателя
