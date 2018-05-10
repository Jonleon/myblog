from django.db import models
from django.urls import reverse
from DjangoUeditor.models import UEditorField
# Create your models here.
class Mytext(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='mypictures/%Y/%m/%d',blank=True)
    content = UEditorField(imagePath="mypictures/%Y/%m/%d",
                           toolbars='besttome',filePath='files/%Y/%m/%d',
                           blank=True,height=300,width=1000)
    updated = models.DateTimeField(auto_now=True)
    likes_number = models.IntegerField(default=0)
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['name']

    def get_absolute_url(self):
        return reverse('blog:artical_by_name',args=[self.id])


