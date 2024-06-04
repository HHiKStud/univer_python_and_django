from django.forms import ModelForm
from .models import NewsPost, Comment
from django import forms

class PostModelForm(ModelForm):
    class Meta:
        model = NewsPost
        fields = [
            'title',
            'content',
            'image']

    def __init__(self, *args, **kwargs):
            super(PostModelForm, self).__init__(*args, **kwargs)
            self.fields['title'].help_text = ""
            self.fields['title'].label = ""
            self.fields['title'].widget = forms.Textarea(
                attrs={
                    'rows': 1,
                    'class': 'form-control',
                    'placeholder': 'Название блога',
                }
            )

            self.fields['content'].help_text = ""
            self.fields['content'].label = ""
            self.fields['content'].widget = forms.Textarea(
                attrs={
                    'rows': 10,
                    'class': 'form-control',
                    'placeholder': 'Содержание',
                }
            )    

class CommentModelForm(ModelForm):
    class Meta:
        model = Comment
        fields = [
           'text']

    def __init__(self, *args, **kwargs):
            super(CommentModelForm, self).__init__(*args, **kwargs)
            self.fields['text'].help_text = ""
            self.fields['text'].label = ""
            self.fields['text'].widget = forms.Textarea(
                attrs={
                    'rows': 1,
                    'class': 'form-control',
                    'placeholder': 'Текст комментария',
                }
            )    
