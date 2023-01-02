from django import forms

class blogform(forms.Form):
    judul = forms.CharField(max_length=50)
    penulis = forms.CharField(max_length=40)
    penerbit = forms.CharField(widget=forms.Textarea)
