from .models import JFSACupMedia
from django import forms

class JFSACupForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['images'] = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

    class Meta:
        model = JFSACupMedia
        fields = '__all__'
