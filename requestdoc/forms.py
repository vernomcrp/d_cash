from django import forms


class InvoiceForm(forms.Form):
    invoice_no = forms.CharField(max_length=50)
    invoice_date = forms.DateTimeField()
    invoice_file = forms.FileField(required=False)
    location_x = forms.CharField(max_length=10)
    location_y = forms.CharField(max_length=10)
    factory_outside = forms.CharField(max_length=150)
    factory_outside_location = forms.CharField(max_length=300)


class ProductForm(forms.Form):
    license_no = forms.CharField(max_length=20)
    standard_industrial_no = forms.CharField(max_length=20)
    standard_name = forms.CharField(max_length=100)
    product_name = forms.CharField(max_length=300)
    quantity = forms.IntegerField()
    unit = forms.CharField(max_length=30)