from django.db import models
from django.utils.translation import ugettext_lazy as _
# from django.conf import settings

# Create your models here.

class Exam(models.Model):
    subject = models.CharField(_("Subject"), max_length=50)
    total_marks = models.CharField(_("Max Marks"), max_length=50)
    time_duration = models.TimeField(_("Time duration"), auto_now=False, auto_now_add=False, blank=True, null=True)
    

    class Meta:
        verbose_name = _("Exam")
        verbose_name_plural = _("Exams")

    def __str__(self):
        return self.subject

    def get_absolute_url(self):
        return reverse("Exam_detail", kwargs={"pk": self.pk})
