from django import forms


class CreatePlace(forms.Form):
    name = forms.CharField(max_length=30)
    location = forms.CharField(max_length=30)
    distance = forms.IntegerField(min_value=0, max_value=999)
    img_url = forms.URLField(max_length=300)
