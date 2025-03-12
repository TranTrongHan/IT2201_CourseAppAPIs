from rest_framework import pagination

class CourserPagination(pagination.PageNumberPagination):
    page_size = 2