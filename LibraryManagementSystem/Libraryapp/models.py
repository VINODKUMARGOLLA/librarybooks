from django.db import models

# Create your models here.
class books(models.Model):
    book_name = models.CharField(max_length=50)
    book_auther_name = models.CharField(max_length=40)
    book_price=models.IntegerField(default=20,null=True)
    book_description = models.TextField(default="Book Details")

    def __str__(self):
        return self.book_name

class new(models.Model):
    pass

    # def __str__(self):
    #     return self

