from django.db import models
from base.models import BaseModel
# Create your models here.
class Like(models.Model):
    post = models.ForeignKey("posts.Post", on_delete=models.CASCADE)
    user = models.OneToOneField("users.User", on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = "Like"
        verbose_name_plural = "Likes"

    def __str__(self):
        return self.name
    
class Post(BaseModel):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images')
    description = models.fields.CharField(max_length=256)
    likes = models.IntegerField() 
    

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        def __str__(self):
            return self.name