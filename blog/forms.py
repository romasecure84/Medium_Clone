from django import forms
from django.core import validators
from .models import BlogPost
from tinymce.widgets import TinyMCE

# Our Validator:
from config.validators import min_length_3

def min_length_3(value):
    if len(value) < 3:
        raise forms.ValidationError('En Az 3 Herfden Ibaret Olmalidir!!')


class BlogPostModelForm(forms.ModelForm):
    tag = forms.CharField(required=False)
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 10, 'rows': 10}))
    # title = forms.CharField(validators=[validators.MinLengthValidator(3, message='En Az 3 Herfden Ibaret Olmalidir!!')])
    title = forms.CharField(validators=[min_length_3,])

    class Meta:
        model = BlogPost
        fields = [
            'title',
            'cover_image',
            'content',
            'category',
            'tag',
        ]

    # def clean_title(self):
    #     title = self.cleaned_data.get('title')
    #     if len(title) < 3:
    #         raise forms.ValidationError('En Az 3 herfden ibaret Olmalidir!')
    #     return title