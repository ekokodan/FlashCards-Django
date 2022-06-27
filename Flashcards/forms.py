from django import forms
from django.forms import ModelForm
from .models import Phrases
from .models import Word


class PhraseForm(ModelForm):
    class Meta:
        model = Phrases
        fields = ('French', 'English', 'Tenses')
        widgets = {
            'English': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter English Phrase',
                                              'autocomplete': 'off'}),
            'French': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter French Translation',
                                             'autocomplete': 'off'}),
            'Tenses': forms.TextInput(attrs={'class': 'form-control',
                                             'placeholder': 'Enter the tense(s) of this Phrase',
                                             'autocomplete': 'off'
                                             })

        }

        labels = {
            'French': '',
            'English': '',
            'Tenses': ''
        }


class WordForm(ModelForm):
    class Meta:
        model = Word
        fields = ('French', 'English', 'Tenses')
        widgets = {
            'French': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter French Translation',
                                             'autocomplete': 'off'}),
            'English': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter English Word',
                                              'autocomplete': 'off'}),
            'Tenses': forms.TextInput(attrs={'class': 'form-control',
                                             'placeholder': 'Enter the tense(s) of this Word',
                                             'autocomplete': 'off'
                                             })

        }

        labels = {
            'French': '',
            'English': '',
            'Tenses': ''
        }
