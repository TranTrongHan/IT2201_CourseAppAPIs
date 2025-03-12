from rest_framework.serializers import ModelSerializer
from courses.models import Course,Category,Lesson,Tag


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name']

class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = ['id','subject','image','created_date','category_id']

class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id','subject','image','created_date']

class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id','name']

class LessonDetailSerializer(ModelSerializer):
    tags = TagSerializer(many=True)
    class Meta:
        model = LessonSerializer.Meta.model
        fields = LessonSerializer.Meta.fields + ['tags','content']