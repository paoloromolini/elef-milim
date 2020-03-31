from django.utils import timezone
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView


from .models import Question, Lesson

class LessonListView(ListView):
    model = Lesson

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class LessonDetailView(DetailView):
    model = Lesson

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context