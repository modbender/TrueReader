from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout
from crispy_forms.bootstrap import InlineCheckboxes

from . import models

class BaseCoreModelForm(forms.ModelForm):

    class Meta:
        abstract = True

class ComicForm(BaseCoreModelForm):

    genres = forms.ModelMultipleChoiceField(
        queryset=models.Genre.objects,
        widget=forms.CheckboxSelectMultiple,
    )

    helper = FormHelper()
    helper.layout = Layout(
        InlineCheckboxes('genres')
    )

    class Meta:
        model = models.Comic
        fields = '__all__'
