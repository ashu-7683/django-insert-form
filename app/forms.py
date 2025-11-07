from django import forms
from app.models import *

class TopicDjForm(forms.Form):
    topic_name=forms.CharField()
    
class WebPageDjForm(forms.Form):
    topic_name=forms.ModelChoiceField(queryset=Topic.objects.all())
    name=forms.CharField()
    url=forms.URLField()
    email=forms.EmailField()
    
class AccessRecordDjForm(forms.Form):
    name=forms.ModelChoiceField(queryset=WebPage.objects.all())
    author=forms.CharField()
    date=forms.DateField()
    
class TopicMF(forms.ModelForm):
    class Meta:
        model=Topic
        fields='__all__'
    
class WebPageMF(forms.ModelForm):
    class Meta:
        model=WebPage
        fields='__all__'
        
class AccessRecordMF(forms.ModelForm):
    class Meta:
        model=AccessRecord
        fields='__all__'