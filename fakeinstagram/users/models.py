from django.contrib.auth.models import AbstractUser, Group,Permission
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from django.db import models
# Create your models here.
class CustomUser(AbstractUser):
    profile_image = models.ImageField(_("profile image"), upload_to="proflie_images", default=None,null=True,blank=True)
    biography = models.CharField(_("biography"), max_length=100, default=None,null=True,blank=True)
    website = models.URLField(_("website"), max_length=200, default=None,null=True,blank=True)
    birth_date = models.DateField(_("birth date"), default=None,null=True,blank=True)
    followed = models.ManyToManyField("users.CustomUser", verbose_name=_("followed"), blank=True)
    SEX_CHOICES = (('M', 'Man'),('W', 'Woman'),('O', 'Other'))
    sex = models.CharField(max_length=1,choices=SEX_CHOICES,default=None)
    
    groups = models.ManyToManyField(Group, related_name='customuser_set', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='customuser_set', blank=True)

    class Meta:
        verbose_name = _("CustomUser")
        verbose_name_plural = _("CustomUsers")

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse("CustomUser_detail", kwargs={"pk": self.pk})
