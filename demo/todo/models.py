from datetime import timezone
from django.db import models
from django.shortcuts import redirect
from django.utils.text import slugify
from django.urls import reverse


class TodoItem(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    completed = models.BooleanField(default=False)
    is_archived = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('todo_detail', kwargs={'slug': self.slug, 'pk': self.id})

    def update(self, completed, *args, **kwargs):
        self.completed = completed
        self.updated_at = timezone.now()
        self.save(*args, **kwargs)
        return redirect(self.get_absolute_url())

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.title
