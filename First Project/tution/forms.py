from django import forms
from .models import Contact, Post

class  ContactForm(forms.ModelForm):
      class Meta:
          model = Contact
          fields = '__all__'


class  PostForm(forms.ModelForm):
      class Meta:
          model = Post
          exclude = ['user', 'id', 'slug', 'created_at']
          widgets={
              'subject':forms.CheckboxSelectMultiple(attrs={
                  'multiple':True,
              }),

            'class_in':forms.CheckboxSelectMultiple(attrs={
                  'multiple':True,
              })
          }