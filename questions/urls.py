from django.urls import path

from .views import LessonDetailView, LessonListView

urlpatterns = [
    path('', LessonListView.as_view(), name='lesson-list'),
    path('<slug:slug>/', LessonDetailView.as_view(), name='lesson-detail'),
]