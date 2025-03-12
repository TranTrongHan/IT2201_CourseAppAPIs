from rest_framework.decorators import action
from rest_framework.response import Response

from courses.models import Course,Category,Lesson,Tag
from rest_framework import viewsets,permissions,generics
from . import serializers,paginators

class CategoryViewSet(viewsets.ViewSet,generics.ListAPIView):
    queryset = Category.objects.filter(active = True)
    serializer_class = serializers.CategorySerializer

class CourseViewSet(viewsets.ViewSet,generics.ListAPIView):
    queryset = Course.objects.filter(active = True)
    pagination_class =paginators.CourserPagination
    serializer_class = serializers.CourseSerializer
    def get_queryset(self):
        queryset = self.queryset
        q = self.request.query_params.get('q')
        if q:
            queryset = queryset.filter(subject__icontains= q)
        cate_id = self.request.query_params.get('category_id')
        if cate_id:
            queryset = queryset.filter(category_id =cate_id )
        return queryset

    @action(methods = ['get'],url_path='lessons',detail = True)
    def get_lessons(self,request,pk):
        lessons = self.get_object().lesson_set.filter(active = True)

        return Response(serializers.LessonSerializer(lessons, many=True).data)

class LessonViewSet(viewsets.ViewSet,generics.RetrieveAPIView):
    queryset = Lesson.objects.prefetch_related('tags').filter(active = True)
    serializer_class = serializers.LessonDetailSerializer

