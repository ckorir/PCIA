from django import forms

cover_choice= [
    ('comprehensive', 'Comprehensive'),
    ('third-party', 'Third-party'),
]

manufacture_year= [tuple([x,x]) for x in range(1950,2023)]


class InquiryForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length =50)
    last_name = forms.CharField(label='Last Name', max_length =50)
    phone_number = forms.DecimalField(label='Phone Number', decimal_places=0, max_digits=15)
    email = forms.EmailField(label='Email')
    location = forms.CharField(label='Location', max_length =50)
    cover_type = forms.CharField(label='Cover Type', max_length =50)
    subject = forms.CharField(label='Subject', max_length =100)
    message = forms.CharField(label='Message', widget=forms.Textarea(attrs={"rows":5, "cols":20}))

class PrivateForm(forms.Form):
    cover_type = forms.CharField(label='Cover Type', widget=forms.Select(choices=cover_choice))
    first_name = forms.CharField(label='First Name', max_length =50)
    last_name = forms.CharField(label='Last Name', max_length =50)
    phone_number = forms.DecimalField(label='Phone Number', decimal_places=0, max_digits=15)
    email = forms.EmailField(label='Email')
    vehicle_make = forms.CharField(label='Vehicle Make', max_length =50)
    vehicle_model = forms.CharField(label='Vehicle Model', max_length =50)
    registration_number = forms.CharField(label='Vehicle Registration Number', max_length =50)
    YOM = forms.DecimalField(label="Year of Manufacture", widget=forms.Select(choices=manufacture_year))
    color = forms.CharField(label='Colour', max_length =50)
    period_from = forms.DateField(label="Period from (YYYY-MM-DD)")
    period_to = forms.DateField(label="To (YYYY-MM-DD)")

class PSVForm(forms.Form):
    cover_type = forms.CharField(label='Cover Type', widget=forms.Select(choices=cover_choice))
    first_name = forms.CharField(label='First Name', max_length =50)
    last_name = forms.CharField(label='Last Name', max_length =50)
    phone_number = forms.DecimalField(label='Phone Number', decimal_places=0, max_digits=15)
    email = forms.EmailField(label='Email')
    vehicle_make = forms.CharField(label='Vehicle Make', max_length =50)
    vehicle_model = forms.CharField(label='Vehicle Model', max_length =50)
    passengers = forms.DecimalField(label='Number of Passengers', decimal_places=0, max_digits=3)
    registration_number = forms.CharField(label='Vehicle Registration Number', max_length =50)
    YOM = forms.DecimalField(label="Year of Manufacture", widget=forms.Select(choices=manufacture_year))
    color = forms.CharField(label='Colour', max_length =50)
    period_from = forms.DateField(label="Period from (YYYY-MM-DD)")
    period_to = forms.DateField(label="To (YYYY-MM-DD)")

class CommercialForm(forms.Form):
    cover_type = forms.CharField(label='Cover Type', widget=forms.Select(choices=cover_choice))
    first_name = forms.CharField(label='First Name', max_length =50)
    last_name = forms.CharField(label='Last Name', max_length =50)
    phone_number = forms.DecimalField(label='Phone Number', decimal_places=0, max_digits=15)
    email = forms.EmailField(label='Email')
    vehicle_make = forms.CharField(label='Vehicle Make', max_length =50)
    vehicle_model = forms.CharField(label='Vehicle Model', max_length =50)
    registration_number = forms.CharField(label='Vehicle Registration Number', max_length =50)
    YOM = forms.DecimalField(label="Year of Manufacture", widget=forms.Select(choices=manufacture_year))
    color = forms.CharField(label='Colour', max_length =50)
    period_from = forms.DateField(label="Period from (YYYY-MM-DD)")
    period_to = forms.DateField(label="To (YYYY-MM-DD)")