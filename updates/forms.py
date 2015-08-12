from django.forms import ModelForm, Textarea
from updates.models import Chirp


class ChirpForm(ModelForm):

    class Meta:
        model = Chirp
        fields = ('title', 'message')
        widgets = {
            'message': Textarea(attrs={'rows':2})
        }