'''
Imports relevant django packages
'''
from django.forms.widgets import ClearableFileInput
from django.utils.translation import gettext_lazy as _


class CustomClearableCocktailFileInput(ClearableFileInput):
    '''
    Custom widget file
    '''
    clear_checkbox_label = _('Remove')
    initial_text = _('Current Image')
    input_text = _('')
    template_name = (
        'cocktails/custom_widget_templates/custom_clearable_file_input.html'
    )
