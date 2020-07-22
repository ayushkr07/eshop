from django.db import models

class Cateogory(models.Model):
    name=models.CharField(max_length=20)

    @staticmethod
    def get_all_cateogories():
        return Cateogory.objects.all()

    def __str__(self):
        return  self.name
