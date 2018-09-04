from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from .models import Bookmark


class BookmarkLV(ListView):
    model = Bookmark


class BookmarkDetailV(DetailView):
    model = Bookmark


class BookmarkUV(UpdateView):
    model = Bookmark
    fields = ['site_name', 'url', 'desc']
    # template_name_suffix = '_update'


class BookmarkDeleteV(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('bookmark:list')


class BookmarkCV(CreateView):
    model = Bookmark
    fields = ['site_name', 'url', 'desc']
    # template_name_suffix = '_create'
    # success_url = reverse_lazy('bookmark:list')

    def get_success_url(self):
        # 방법1
        return reverse('bookmark:detail', args=[self.object.id])
        # return reverse('bookmark:detail', kwargs={'pk': self.object.id})       # 방법3
        # return reverse_lazy('bookmark:detail', args=[self.object.id])          # 방법2
        # return reverse_lazy('bookmark:detail', kwargs={'pk': self.object.id})  # 방법4
