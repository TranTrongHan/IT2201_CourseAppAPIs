from django.contrib import admin
from .models import Category,Course,Lesson,Tag
from django.utils.safestring import mark_safe
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class LessonForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget)
    class Meta:
        model = Lesson
        fields = '__all__'


class MyLessonAdmin(admin.ModelAdmin):
    readonly_fields = ['image_view']
    def image_view(self,lesson):
        return mark_safe(f"<img src='/static/{lesson.image.name}' width='200' />")

    form = LessonForm

    class Media:
        css ={
            'all':('/static/css/style.css')
        }

admin.site.register(Category)
admin.site.register(Course)
admin.site.register(Lesson,MyLessonAdmin)
admin.site.register(Tag)