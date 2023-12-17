from django import forms
from explore.models import Hotel

class HotelSubmissionForm(forms.ModelForm):

    class Meta:
        model = Hotel
        exclude = ['owner','license_verified']

    def __init__(self, *args, **kwargs):
        super(HotelSubmissionForm, self).__init__(*args, **kwargs)
        self.fields['license_number'].widget.attrs['placeholder'] = 'Enter License Number'
        self.fields['desc'].widget.attrs['style'] = 'width: 100%;'
     
    submitted = forms.BooleanField(
        label='Do you want to submit?',
        required=False,  # Since it's a checkbox, it can be optional
        widget=forms.CheckboxInput(attrs={'class': 'checkbox-input'}),
    )
        





