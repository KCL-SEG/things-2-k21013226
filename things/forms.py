"""Forms of the project."""

# Create your forms here.

from django import forms


class ThingForm(forms.Form):
    name = forms.CharField(label = "Enter Name",max_length=35)
    description = forms.CharField(label = "Enter Description",max_length=120)
    quantity =  forms.IntegerField(label = "Enter Quantity")


#The form must accept valid inputs for Thing and reject invalid input for Thing.

#The description field must be displayed as a Textarea. The quantity field must be displayed as NumberInput.
"""
name = models.CharField(max_length=35, unique=True)
    description = models.CharField(max_length=120, blank=True)
    quantity = models.IntegerField(
        validators=[MinValueValidator(0),MaxValueValidator(50)]
    )

"""