from django import forms
from ckeditor.widgets import CKEditorWidget


class TextToHtmlForm(forms.Form):
    content = forms.CharField(widget=CKEditorWidget(), label='')