from django.db import models

# Create your models here.
class article(models.Model):
    title = models.CharField('title', max_length=50,)
    announse = models.CharField('Anons', max_length=250)
    full_text = models.TextField('Text')
    date = models.DateTimeField('Time')

    def __str__(self) -> str:
        return self.title