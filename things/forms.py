"""Forms of the project."""

# Create your forms here.


from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator

description = models.CharField(max_length=120, blank=True)

class ThingForm(forms.Form):
    name = forms.CharField(label = "Enter Name",max_length=35)
    description = forms.CharField(widget=forms.Textarea[maxlength=="120"])
    quantity =  forms.IntegerField(label = "Enter Quantity",validators=[MinValueValidator(0),MaxValueValidator(50)])

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
