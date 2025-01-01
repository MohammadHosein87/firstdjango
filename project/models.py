from django.db import models


class Post(models.Model):
    عنوان = models.CharField(max_length=100)
    محتوا = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.عنوان
