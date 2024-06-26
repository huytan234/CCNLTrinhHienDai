from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework import routers
from course import views

r = routers.DefaultRouter()
r.register('categories', views.CategoryViewSet, 'categories')
r.register('course', views.CourseViewSet, 'Course')
r.register('lessons', views.LessonViewSet, 'Lesson')
r.register('users', views.UserViewSet, 'User')
r.register('comments', views.CommentViewSet, 'comments')


urlpatterns = [
    path('', include(r.urls))
]