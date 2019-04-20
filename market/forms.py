from django import forms
from .models import Day


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


class DomesticSecurietiesForm(forms.Form):
    d_barclays_checkbox = forms.BooleanField(required=False)
    d_bihl_checkbox = forms.BooleanField(required=False)
    d_choppies_checkbox = forms.BooleanField(required=False)
    d_cresta_checkbox = forms.BooleanField(required=False)
    d_engen_checkbox = forms.BooleanField(required=False)
    d_fnbb_checkbox = forms.BooleanField(required=False)
    d_furnmart_checkbox = forms.BooleanField(required=False)
    d_g4s_checkbox = forms.BooleanField(required=False)
    d_letlole_checkbox = forms.BooleanField(required=False)
    d_letshego_checkbox = forms.BooleanField(required=False)
    d_minergy_checkbox = forms.BooleanField(required=False)
    d_nap_checkbox = forms.BooleanField(required=False)
    d_olympia_checkbox = forms.BooleanField(required=False)
    d_primetime_checkbox = forms.BooleanField(required=False)
    d_rcdp_checkbox = forms.BooleanField(required=False)
    d_sechaba_checkbox = forms.BooleanField(required=False)
    d_seedco_checkbox = forms.BooleanField(required=False)
    d_sefalana_checkbox = forms.BooleanField(required=False)
    d_stanchart_checkbox = forms.BooleanField(required=False)
    d_turnstar_checkbox = forms.BooleanField(required=False)

    def __init__(self, *args, **kwargs):
        super(DomesticSecurietiesForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'domesticStocks'

class IndexSecurietiesForm(forms.Form):
    i_barclays_checkbox = forms.BooleanField(required=False)
    i_bihl_checkbox = forms.BooleanField(required=False)
    i_choppies_checkbox = forms.BooleanField(required=False)
    i_cresta_checkbox = forms.BooleanField(required=False)
    i_engen_checkbox = forms.BooleanField(required=False)
    i_fnbb_checkbox = forms.BooleanField(required=False)
    i_furnmart_checkbox = forms.BooleanField(required=False)
    i_g4s_checkbox = forms.BooleanField(required=False)
    i_letlole_checkbox = forms.BooleanField(required=False)
    i_letshego_checkbox = forms.BooleanField(required=False)
    i_minergy_checkbox = forms.BooleanField(required=False)
    i_nap_checkbox = forms.BooleanField(required=False)
    i_olympia_checkbox = forms.BooleanField(required=False)
    i_primetime_checkbox = forms.BooleanField(required=False)
    i_rcdp_checkbox = forms.BooleanField(required=False)
    i_sechaba_checkbox = forms.BooleanField(required=False)
    i_seedco_checkbox = forms.BooleanField(required=False)
    i_sefalana_checkbox = forms.BooleanField(required=False)
    i_stanchart_checkbox = forms.BooleanField(required=False)
    i_turnstar_checkbox = forms.BooleanField(required=False)

    def __init__(self, *args, **kwargs):
        super(IndexSecurietiesForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'indexfield'
