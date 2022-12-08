"""Forms of the project."""

# Create your forms here.


from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator


class ThingForm(forms.Form):
    name = forms.CharField(label = "Enter Name",max_length=35)
    description = forms.CharField(widget=forms.Textarea)
    quantity =  forms.IntegerField(label = "Enter Quantity",validators=[MinValueValidator(0),MaxValueValidator(50)])
