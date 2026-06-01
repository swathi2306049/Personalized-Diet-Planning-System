from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ['username','full_name','email','goal',
        'health_condition','profile_completed']
    list_filter = ['goal','health_condition','is_gym_freak','profile_completed']
    fieldsets = UserAdmin.fieldsets + (
        ('Health & Profile', {'fields': (
            'full_name','profile_photo','date_of_birth','gender','phone',
            'height_cm','weight_kg','target_weight_kg','health_condition',
            'other_health_condition','activity_level','diet_type','allergies',
            'goal','is_gym_freak','gym_days_per_week','preferred_workout',
            'wake_up_time','sleep_time','meals_per_day','water_intake_liters',
            'profile_completed',
        )}),
    )
