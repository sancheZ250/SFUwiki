from rest_framework.pagination import PageNumberPagination


class AllTeacherPagination(PageNumberPagination):
    page_size = 2
