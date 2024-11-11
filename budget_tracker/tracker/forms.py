from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Transaction

class TransactionForm(forms.ModelForm):
    amount = forms.DecimalField(
        label="Amount (₹)",
        max_digits=10,
        decimal_places=2,
        required=True
    )
    date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}), 
        required=True
    )

    class Meta:
        model = Transaction
        fields = ['category', 'amount', 'date', 'description']

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
