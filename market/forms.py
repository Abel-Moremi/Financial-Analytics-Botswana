from django import forms
from .models import Day, BarclaysDaily


class DateInput(forms.DateInput):
    input_type = 'date'


class DayAdminForm(forms.ModelForm):

    class Meta:
        model = Day
        fields = ['date', ]

    date = forms.DateField(
        widget=forms.DateInput(format='%d-%b-%Y', attrs={'class': 'datepicker'}),
        input_formats=('%d-%b-%Y', )
    ), DateInput()


class BarclaysAdminForm(forms.ModelForm):

    class Meta:
        model = BarclaysDaily
        fields = ['date', ]

    date = forms.DateField(
        widget=forms.DateInput(format='%d-%b-%Y', attrs={'class': 'datepicker'}),
        input_formats=('%d-%b-%Y', )
    ), DateInput()
