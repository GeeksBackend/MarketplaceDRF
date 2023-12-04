from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Название"
    )
    description = models.TextField(
        max_length=500,
        verbose_name="Описание"
    )
    image = models.ImageField(
        upload_to="post_images/",
        verbose_name="Фотография"
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания"
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"