from django import forms


class CouponAppyForm(forms.Form):
    code = forms.CharField()
