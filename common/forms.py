from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserForm(UserCreationForm):
    email = forms.EmailField(label="이메일")
    '''
    pin = forms.DecimalField(label="기기 핀번호")
    height = forms.DecimalField(label="키")
    weight = forms.DecimalField(label="몸무게")
    '''

    class Meta:
        model = User
        fields = ("username", "email")
        '''
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'pin': forms.NumberInput(attrs={'class': 'form-control'}),
            'height': forms.NumberInput(attrs={'class': 'form-control'}),
            'weight': forms.NumberInput(attrs={'class': 'form-control'}),
        }
        '''

    '''
    def save(self, commit=True):  # 저장하는 부분 오버라이딩
        user = super(UserForm, self).save(commit=False)  # 본인의 부모를 호출해서 저장하겠다.
        user.email = self.cleaned_data["email"]
        
        user.pin = self.cleaned_data["pin"]
        user.height = self.cleaned_data["height"]
        user.weight = self.cleaned_data["weight"]
        
        if commit:
            user.save()
        return user
    '''
