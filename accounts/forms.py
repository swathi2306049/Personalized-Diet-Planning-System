from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    full_name = forms.CharField(max_length=150)
    class Meta:
        model = CustomUser
        fields = ['username','full_name','email','password1','password2']

class LoginForm(AuthenticationForm):
    pass

class ProfileForm(forms.ModelForm):
    date_of_birth = forms.DateField(
        widget=forms.DateInput(attrs={'type':'date'}), required=False)
    wake_up_time = forms.TimeField(
        widget=forms.TimeInput(attrs={'type':'time'}), required=False)
    sleep_time = forms.TimeField(
        widget=forms.TimeInput(attrs={'type':'time'}), required=False)
    class Meta:
        model = CustomUser
        fields = ['full_name','profile_photo','date_of_birth','gender','phone',
            'height_cm','weight_kg','target_weight_kg','health_condition',
            'other_health_condition','activity_level','diet_type','allergies',
            'goal','is_gym_freak','gym_days_per_week','preferred_workout',
            'wake_up_time','sleep_time','meals_per_day','water_intake_liters'
        ]