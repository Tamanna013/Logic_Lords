# text_analysis/forms.py
from django import forms

class TextUploadForm(forms.Form):
    text_file = forms.FileField()
