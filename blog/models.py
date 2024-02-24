from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200, blank=False, null=False)
    content = models.TextField(blank=False, null=False)
    time = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='photo/')
    email = models.EmailField(
        max_length=54, blank=True, null=False, default="excelnandhu@gmail.com")

    def get_image_url(self):
        return self.photo.url

    def __str__(self) -> str:
        return f'Title: {self.title}, Characters: {len(self.content)}'
