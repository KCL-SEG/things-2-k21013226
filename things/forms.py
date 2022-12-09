"""Forms of the project."""

# Create your forms here.

from .models import Thing
from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator


class ThingForm(forms.ModelForm):
    class Meta:
        model = Thing
        fields = ["name","description","quantity"]
        widgets = {'description':forms.Textarea() }








    #name = forms.CharField(label = "Enter Name",max_length=35)
    #description = forms.CharField(widget=forms.Textarea[max_length =="120"])
    #quantity =  forms.IntegerField(label = "Enter Quantity",validators=[MinValueValidator(0),MaxValueValidator(50)])

#with_asserts.context_manager.SelectorNotFound: No selector matches found for textarea[maxlength="120"]
#AssertionError: Could not find an input matching the specifications of the description field.

"""
    class Meta:
        model = Thing
        fields = ["name","description","quantity"]

        widgets = {
            'description': forms.Textarea(attrs={
            'maxlength': 120,
            }

            )

        }
"""
