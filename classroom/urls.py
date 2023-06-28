from django.urls import path

from classroom.views import LessonListView, LessonDetailView, LessonCreateView, LessonDeleteView

# LessonCreateView

urlpatterns = [
    path('', LessonListView.as_view(), name='list-lesson'),
    path('<slug:slug>/', LessonDetailView.as_view(), name='detail-lesson'),
    path('new-lesson/', LessonCreateView.as_view(), name='new-lesson'),
    path('lesson/<pk>/', LessonDeleteView.as_view(), name='delete-lesson'),
]
