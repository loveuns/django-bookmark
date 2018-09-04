from django.db import models
from django.urls import reverse_lazy, reverse


class Bookmark(models.Model):
    site_name = models.CharField(max_length=100)
    url = models.URLField('Site URL')
    desc = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['site_name']

    def __str__(self):
        return self.site_name + " - " + self.url

    def get_absolute_url(self):
        return reverse('bookmark:detail', args=[self.id])
        # return reverse('bookmark:detail', kwargs={'pk': self.id})
        # return reverse_lazy('bookmark:detail', args=[self.id])
        # return reverse_lazy('bookmark:detail', kwargs={'pk': self.id})
