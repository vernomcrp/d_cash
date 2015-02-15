from django import forms


class InvoiceForm(forms.Form):
    invoice_no = forms.CharField(max_length=50, label='Invoice No.')
    invoice_date = forms.DateField(label="Invoice Date (YYYY-MM-DD")
    invoice_file = forms.FileField(required=False, label='Input File')
    location_x = forms.CharField(max_length=10, label='Location X')
    location_y = forms.CharField(max_length=10, label='Location Y')
    factory_outside = forms.CharField(max_length=150, label='Factory Name (Outside country)')
    factory_outside_location = forms.CharField(max_length=300, label='Factory Location (Outside country)')


class ProductForm(forms.Form):
    license_no = forms.CharField(max_length=20, label='License No.')
    standard_industrial_no = forms.CharField(max_length=20, label='Std. Industrial No.')
    standard_name = forms.CharField(max_length=100, label='Std. Name')
    product_name = forms.CharField(max_length=300, label='Product Name')
    quantity = forms.IntegerField(label='Quantity')
    unit = forms.CharField(max_length=30, label='Product Unit')
    hs_code = forms.CharField(max_length=30, label='HS Code')