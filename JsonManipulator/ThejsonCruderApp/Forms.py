from django import forms

class JsonFileUploadForm(forms.Form):
    json_file = forms.FileField()
