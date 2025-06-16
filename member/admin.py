from django.contrib import admin

from member.models import Client, ProjectImage
from blogs.models import Blog
from course.models import Course,Module

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1

class ClientAdmin(admin.ModelAdmin):
    list_display = ('client_code', 'name', 'contact', 'project_status')
    inlines = [ProjectImageInline]

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status', 'published_date')
    prepopulated_fields = {'slug': ('title',)}


class ModuleInline(admin.TabularInline):
    model = Module
    extra = 1

class CourseAdmin(admin.ModelAdmin):
    inlines = [ModuleInline]
    list_display = ('name', 'duration')

admin.site.register(Course, CourseAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Blog, BlogAdmin)
