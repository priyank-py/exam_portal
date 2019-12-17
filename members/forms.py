from django import forms
from .models import Member


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ('user', 'about', 'image')
    
    def clean_about(self, *args, **kwargs):
        content = self.cleaned_data.get('about')
        if len(content) > 140:
            raise forms.ValidationError('About too long..')
        return content


    def clean(self, *args, **kwargs):
        data = self.cleaned_data
        content = data.get('about', None)
        if content == "":
            content = None
        image = data.get('image', None)
        if content is None and image is None:
            raise forms.ValidationError('content or image is required')
        return super().clean(*args, **kwargs)