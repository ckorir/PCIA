from django import forms

class InquiryForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length =30)
    last_name = forms.CharField(label='Last Name', max_length =30)
    phone_number = forms.IntegerField(label='Phone Number')
    email = forms.EmailField(label='Email')
    subject = forms.CharField(label='Subject', max_length =100)
    location = forms.CharField(label='Location', max_length =30)
    cover_type = forms.CharField(label='Cover Type', max_length =30)
    message = forms.CharField(label='Message', max_length =500)