from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

def upload_profile_pic(instance, filename):
    return f"profile/{instance.user}/{filename}"

class Member(models.Model):
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    about = models.TextField(_("About you"))
    image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None, blank=True, null=True)
    

    class Meta:
        verbose_name = _("Member")
        verbose_name_plural = _("Members")

    def __str__(self):
        return self.user.username

