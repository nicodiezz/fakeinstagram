from django.contrib.auth.models import AbstractUser, Group,Permission
from django.utils.translation import gettext_lazy as _
from django.db import models
from fakeinstagram.settings import AUTH_USER_MODEL
from django.contrib.auth.models import UserManager
# Create your models here.
class CustomUser(AbstractUser):
    profile_picture = models.ImageField(_("profile picture"), upload_to="profile_picture", default=None,null=True,blank=True)
    biography = models.CharField(_("biography"), max_length=100, default=None,null=True,blank=True)
    website = models.URLField(_("website"), max_length=200, default=None,null=True,blank=True)
    birth_date = models.DateField(_("birth date"), default=None,null=True,blank=True)
    
    following_count = models.IntegerField(default = 0, null=True,blank=True)
    followers_count = models.IntegerField(default = 0, null=True,blank=True) 
    posts_count = models.IntegerField(default = 0, null=True,blank=True)   
    
    following = models.ManyToManyField('self', verbose_name=_("following"), blank=True, default = None)

    #this fields are included to avoid exceptions
    
    groups = models.ManyToManyField(Group, related_name='customuser_set', blank=True, default = None)
    user_permissions = models.ManyToManyField(Permission, related_name='customuser_set', blank=True, default = None)
    objects = UserManager()
    class Meta:
        verbose_name = _("CustomUser")
        verbose_name_plural = _("CustomUsers")

    def __str__(self):
        return self.username
