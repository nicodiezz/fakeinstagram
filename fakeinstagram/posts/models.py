from django.db import models
from base.models import BaseModel
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
# Create your models here.
class Like(models.Model):
    post = models.ForeignKey("posts.Post", on_delete=models.CASCADE)
    user = models.ForeignKey("users.CustomUser", on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = _("Like")
        verbose_name_plural = _("Likes")  
    
class Post(BaseModel):
    user = models.ForeignKey("users.CustomUser", on_delete=models.CASCADE)
    image = models.ImageField(upload_to='posts')
    description = models.fields.CharField(max_length=256)
    likes = models.IntegerField() 
    
    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")
    def __str__(self):
        return f"{self.user.username}'s post"