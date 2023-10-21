from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter, SimpleRouter
from rest_framework_nested import routers
from .views import InstituteViewSet, DepartmentViewSet, TeacherViewSet, DisciplineViewSet, \
 TeachersByDepartmentList, ModerTeacherViewSet, TeacherReviewList, TeacherReviewDetail

router = DefaultRouter()
router.register(r'institutes', InstituteViewSet)

institute_router = routers.NestedSimpleRouter(router, r'institutes', lookup='institute')
institute_router.register(r'departments', DepartmentViewSet, basename='institute_departments')
institute_router.register(r'teachers', TeacherViewSet, basename='institute_teachers')
institute_router.register(r'moderate-teachers', ModerTeacherViewSet, basename='institute_moder_teachers')
router.register(r'disciplines', DisciplineViewSet, basename='disciplines')

urlpatterns = [
    path('api/v1/teachers/<int:teacher_id>/reviews/', TeacherReviewList.as_view(), name='teacher_reviews_list'),
    path('api/v1/teachers/<int:teacher_id>/reviews/<int:id>/', TeacherReviewDetail.as_view(),
         name='teacher_review_detail'),
    path('api/v1/', include(router.urls)),
    path('api/v1/', include(institute_router.urls)),
    path('api/v1/departments/<int:department_id>/teachers/', TeachersByDepartmentList.as_view(),
         name='teachers-by-department-list'),
]

# api/v1/institutes/ - список институтов. api/v1/institutes/<institute_id>/ - информация о конкретном институте.
# api/v1/institutes/<institute_id>/departments/ - список кафедр в институте.
# api/v1/institutes/<institute_id>/departments/<department_id>/ - информация о конкретной кафедре.
# api/v1/institutes/<institute_id>/teachers/ - список преподавателей в институте.
# api/v1/institutes/<institute_id>/teachers/<teacher_id>/ - информация о конкретном преподавателе.
# api/v1/disciplines/ - список дисциплин api/v1/disciplines/<discipline_id>/ - Информация о конкретной дисциплине
# api/v1/teachers/<teacher_id>/reviews/ - Информация о отзывах на преподавателя, сюда же post запрос на добавление
# нового отзыва
# api/v1/teachers/<teacher_id>/reviews/<review_id> - Информация о конкретном отзыве(GET),
# изменение и удаление(POST,DELETE)
# api/v1/departments/<int:department_id>/teachers/ - Список преподавателей по id кафедры, возвращает первые фото,
# имена и id института преподавателя с его рейтингами