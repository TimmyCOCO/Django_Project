from django.db import models

# Create your models here.

class BookInfo(models.Model):
    title=models.CharField(max_length=20)
    pub_date = models.DateField()

    # show book_title in hero_info
    def __str__(self):
        return self.title

class HeroInfo(models.Model):
    name = models.CharField(max_length=10)
    content=models.CharField(max_length=20)
    gender=models.BooleanField(default=True)
    book=models.ForeignKey(BookInfo, on_delete=models.CASCADE)