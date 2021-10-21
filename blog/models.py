from django.db import models

# Create your models here.
class Blog(models.Model):
    ad=models.CharField(max_length=127,null=True,blank=True)
    soyad=models.CharField(max_length=127,null=True,blank=True)
    #text=models.TextField(help_text='bura melumat daxil et')
    tarix=models.DateTimeField(auto_now_add=True)

    def __str__(self):
         return self.ad        # admin sehifesinde titleler gorunsun