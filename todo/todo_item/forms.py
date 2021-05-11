from django import forms
from todo_item.models import ListItem
from django.core.exceptions import NON_FIELD_ERRORS


class ItemForm(forms.ModelForm):

    expare_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        required=False
    )

    class Meta:
        model = ListItem
        fields = ('name', 'list_model', 'expare_date')
        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "Такое дело уже существует",
            }
        }
