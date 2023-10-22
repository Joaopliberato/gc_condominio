from typing import Any
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.contrib import messages

class IndexView(TemplateView):
    template_name = 'index.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        return context
