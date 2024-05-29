from django.db import models
from base.models import BaseModel
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from fakeinstagram.settings import AUTH_USER_MODEL
# Create your models here.
class Like(models.Model):
    post = models.ForeignKey("posts.Post", on_delete=models.CASCADE)
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = _("Like")
        verbose_name_plural = _("Likes")  
    
class Post(BaseModel):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='posts/')
    description = models.fields.CharField(max_length=256,null=True, blank=True)
    likes_count = models.IntegerField(default=0, null=True, blank=True) 
    
    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")
    def __str__(self):
        return f"{self.user.username}'s post"

class Comment(BaseModel):
    post = models.ForeignKey("posts.Post", on_delete=models.CASCADE)
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.CharField(max_length=256)
 
    class Meta:
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse("Comment_detail", kwargs={"pk": self.pk})
