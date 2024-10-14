from .models import Comment, Location
from django import forms
from django_summernote.widgets import SummernoteWidget


class CommentForm(forms.ModelForm):
    """
    This class sets up the Comment Form and allows some
    customizations of attributes
    """
    class Meta:
        model = Comment
        fields = ('body',)

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['body'].label = "Your comments..."


class LocationForm(forms.ModelForm):
    """
    This class sets up the Location Form and allows some
    customizations of attributes
    """
    class Meta:
        model = Location
        fields = ('title', 'region', 'body', 'location_image', 'status')
        widgets = {
            'body': SummernoteWidget()
        }

    def __init__(self, *args, **kwargs):
        super(LocationForm, self).__init__(*args, **kwargs)
        self.fields[
            'location_image'
            ].label = "Please upload a photo of location here!"
        self.fields['status'].label = "Publish or Save Draft"