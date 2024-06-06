from allauth.account.forms import SignupForm
from django import forms


class CustomUserForm(SignupForm):
    age = forms.IntegerField(label='Возраст')
    country = forms.CharField(max_length=100, label='Город')
    phone_number = forms.CharField(max_length=15, required=False, label='Телефон номер')

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if phone_number and len(phone_number) != 9:
            raise forms.ValidationError('Номер телефона должен состоять из 9 символов.')
        return phone_number

    def save(self, request):
        user = super(CustomUserForm, self).save(request)
        phone_number = self.cleaned_data['phone_number']
        user.phone_number = "+996" + phone_number
        user.age = self.cleaned_data['age']
        user.country = self.cleaned_data['country']
        user.save()
        return user