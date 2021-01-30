from django.forms import ModelForm

from models import Poll


class CreatePollForm(ModelForm):
    class Meta:
        fields = ['question', 'option_one', 'options_two', 'options_three']
