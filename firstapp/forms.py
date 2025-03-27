from django import forms
from .models import Destination,News
class DestinationForm(forms.ModelForm):
    class Meta:
        model = Destination
        fields = ['title', 'description','image_url']


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        exclude = ('created_at',)

        fields = ['title', 'description','image_url','created_at']

        #from django import form
        #from .models import Destination
        #class DestinationForm(forms.ModelForm):
        #class Meta:
        #model=Destination
        #fields=['']