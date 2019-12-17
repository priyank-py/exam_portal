from django.contrib import admin
from .models import Member
from .forms import MemberForm

class MemberAdmin(admin.ModelAdmin):
    list_display = ['user', 'about', 'image']
    form = MemberForm
    # class Meta:
    #     model = MemberForm

admin.site.register(Member, MemberAdmin)
