from django.urls import path, include
from . import views
from rest_framework import routers


routers = routers.DefaultRouter()
routers.register('categories',views.CategoryViewSet,'category')
routers.register('courses',views.CourseViewSet,'course')
routers.register('lessons',views.LessonViewSet,'lesson')

urlpatterns = [
    path('', include(routers.urls))
]
