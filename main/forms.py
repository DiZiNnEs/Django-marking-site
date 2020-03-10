from .models import Notes, Contact, About
from django.forms import ModelForm
from .models import Notes


class EntryNotes(ModelForm):
    class Meta:
        model = Notes
        fields = ('text', 'user')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text'].widget.attrs.update(
            {'class': 'textarea', 'placeholder': 'What\'s your on mind??', 'cols': '100', 'rows': '10'})
