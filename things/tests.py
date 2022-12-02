from django.test import TestCase

# Create your tests here.
from django import forms
from with_asserts.case import TestCase
from django.urls import reverse
from things.forms import ThingForm

from django.test import TestCase



class HomeViewTestCase(TestCase):
    def setUp(self):
        self.url = reverse('home')

    def test_get_home_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_home_has_csrf_token(self):
        response = self.client.get(self.url)
        try:
            with self.assertHTML(response, 'input[name="csrfmiddlewaretoken"]') as (element,):
                self.assertEqual(element.type, 'hidden')
        except:
            self.fail("Could not find csrf_token in the view!  Did you forget to add the csrf_token?")

    def test_home_has_name(self):
        response = self.client.get(self.url)
        try:
            with self.assertHTML(response, 'input[type="text"][maxlength="35"]') as (element,):
                pass
        except:
            self.fail("Could not find an input matching the specifications of the name field.")

    def test_home_has_description(self):
        response = self.client.get(self.url)
        try:
            with self.assertHTML(response, 'textarea[maxlength="120"]') as (element,):
                pass
        except:
            self.fail("Could not find an input matching the specifications of the description field.")

    def test_home_has_quantity(self):
        response = self.client.get(self.url)
        try:
            with self.assertHTML(response, 'input[type="number"]') as (element,):
                pass
        except:
            self.fail("Could not find an input matching the specifications of the quantity field.")

    def test_home_has_submit(self):
        response = self.client.get(self.url)
        try:
            with self.assertHTML(response, '[type="submit"]') as (element,):
                pass
        except:
            self.fail("Could not find a submit button or input in the form!  Did you forget the submit button at the bottom of the form?")

class ThingFormTestCase(TestCase):
    def setUp(self):
        super().setUp()
        self.input = {
            'name': 'Thing',
            'description': "Thing's description",
            'quantity': 2
        }

    def test_valid_form(self):
        form = ThingForm(data=self.input)
        self.assertTrue(form.is_valid())

    def test_form_has_name_field(self):
        form = ThingForm()
        self.assertIn('name', form.fields.keys())

    def test_form_has_description_field(self):
        form = ThingForm()
        self.assertIn('description', form.fields.keys())
        field = form.fields['description']
        self.assertTrue(isinstance(field.widget, forms.Textarea))

    def test_form_has_quantity_field(self):
        form = ThingForm()
        self.assertIn('quantity', form.fields.keys())
        field = form.fields['quantity']
        self.assertTrue(isinstance(field.widget, forms.NumberInput))

    def test_form_has_no_created_at_field(self):
        form = ThingForm()
        self.assertNotIn('created_at', form.fields.keys())

    def test_form_name_can_be_35_characters(self):
        self.input['name'] = 'x' * 35
        form = ThingForm(data=self.input)
        self.assertTrue(form.is_valid())

    def test_form_name_cannot_be_36_characters(self):
        self.input['name'] = 'x' * 36
        form = ThingForm(data=self.input)
        self.assertFalse(form.is_valid())

    def test_form_quantity_cannot_be_negative(self):
        self.input['quantity'] = -1
        form = ThingForm(data=self.input)
        self.assertFalse(form.is_valid())

    def test_form_quantity_can_be_0(self):
        self.input['quantity'] = 0
        form = ThingForm(data=self.input)
        self.assertTrue(form.is_valid())

    def test_form_quantity_cannot_be_over_50(self):
        self.input['quantity'] = 50
        form = ThingForm(data=self.input)
        self.assertTrue(form.is_valid())

    def test_form_quantity_cannot_be_over_50(self):
        self.input['quantity'] = 51
        form = ThingForm(data=self.input)
        self.assertFalse(form.is_valid())