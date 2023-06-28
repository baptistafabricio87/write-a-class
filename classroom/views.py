from django.views.generic import ListView, CreateView, DetailView, DeleteView

from classroom.models import Lesson


class LessonCreateView(CreateView):
    model = Lesson
    template_name = 'new-class.html'


class LessonListView(ListView):
    model = Lesson
    template_name = 'last-classes.html'
    context_object_name = 'lesson'


class LessonDetailView(DetailView):
    model = Lesson
    template_name = 'class.html'
    context_object_name = 'lesson'


class LessonDeleteView(DeleteView):
    model = Lesson
