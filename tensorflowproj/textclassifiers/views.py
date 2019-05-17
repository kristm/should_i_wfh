# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse

from django.views.generic import TemplateView
from textclassifiers.forms import ClassifyForm

# Create your views here.
class ClassifyView(TemplateView):
    template_name = 'textclassifiers/classify.html'

    def get(self, request):
        form = ClassifyForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = ClassifyForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['post']

        args = {'form': form, 'text': text}
        return render(request, self.template_name, args)