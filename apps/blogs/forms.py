from django import forms
from django.contrib.auth.models import User
from .models import Blog
from ckeditor.widgets import CKEditorWidget


class BlogForm(forms.ModelForm):

    title = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'required': 'true', 'class': 'form-control',
               'placeholder': 'Title'}))
    body = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Blog
        exclude = ['id', 'created_at']

    def __init__(self, request, *args, **kwargs):
        super(BlogForm, self).__init__(*args, **kwargs)
        self.fields['creator'].initial = request.user


class BlogEditForm(forms.ModelForm):

    title = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'required': 'true', 'class': 'form-control',
               'placeholder': 'Title'}))
    body = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Blog
        exclude = ['id', 'created_at']

    def __init__(self, request, *args, **kwargs):
        super(BlogEditForm, self).__init__(*args, **kwargs)
        self.fields['creator'].initial = request.user
        self.fields['title'].widget.attrs['readonly'] = True
