from django import forms
from django.utils.translation import ugettext_lazy as _

METHODS = (
    ("nltk", _("Natural Language Toolkit (keywords + bi-grams)")),
    ("pure", _("Simple word frequency analysis")),
    ("calais", _("Calais API tags (english, french and spanish only)"))
)
class KeywordForm(forms.Form):
    text = forms.CharField(label=_("Text to analyze"), widget=forms.Textarea)
    method = forms.ChoiceField(label=_("Method"), choices=METHODS)

    def __init__(self, *args, **kwargs):
        super(KeywordForm, self).__init__(*args, **kwargs)
        self.fields["text"].widget.attrs['placeholder'] = _("Paste your text here...")