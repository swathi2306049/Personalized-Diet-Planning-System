from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Basic Info
    full_name = models.CharField(max_length=150, blank=True)
    profile_photo = models.ImageField(upload_to='profiles/', blank=True, null=True)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=20, choices=[
        ('male','Male'),('female','Female'),('other','Other')], blank=True)
    phone = models.CharField(max_length=15, blank=True)

    # Physical Info
    height_cm = models.FloatField(null=True, blank=True)
    weight_kg = models.FloatField(null=True, blank=True)
    target_weight_kg = models.FloatField(null=True, blank=True)

    # Health
    HEALTH_CHOICES = [('none','None'),('diabetes','Diabetes'),
        ('hypertension','High BP'),('thyroid','Thyroid'),
        ('pcod','PCOD'),('pcos','PCOS'),('cholesterol','High Cholesterol'),
        ('heart','Heart Condition'),('anemia','Anemia'),('obesity','Obesity')]
    health_condition = models.CharField(max_length=50,
        choices=HEALTH_CHOICES, default='none')
    other_health_condition = models.CharField(max_length=200, blank=True)

    # Lifestyle
    ACTIVITY_CHOICES = [('sedentary','Sedentary'),('light','Lightly Active'),
        ('moderate','Moderately Active'),('very_active','Very Active'),
        ('extra_active','Extra Active')]
    activity_level = models.CharField(max_length=30,
        choices=ACTIVITY_CHOICES, default='moderate')

    DIET_CHOICES = [('veg','Vegetarian'),('non_veg','Non-Vegetarian'),
        ('vegan','Vegan'),('eggetarian','Eggetarian')]
    diet_type = models.CharField(max_length=20,
        choices=DIET_CHOICES, default='veg')
    allergies = models.TextField(blank=True)

    # Goal
    GOAL_CHOICES = [('weight_loss','Weight Loss'),('weight_gain','Weight Gain'),
        ('maintain','Maintain'),('muscle_gain','Muscle Gain'),
        ('health_condition','Manage Condition'),('general','General')]
    goal = models.CharField(max_length=30, choices=GOAL_CHOICES, default='general')

    # Gym
    is_gym_freak = models.BooleanField(default=False)
    gym_days_per_week = models.IntegerField(null=True, blank=True)
    preferred_workout = models.CharField(max_length=100, blank=True)

    # Routine
    wake_up_time = models.TimeField(null=True, blank=True)
    sleep_time = models.TimeField(null=True, blank=True)
    meals_per_day = models.IntegerField(default=3)
    water_intake_liters = models.FloatField(null=True, blank=True)

    # Saved recipes
    saved_recipes = models.ManyToManyField('recipes.Recipe',
        blank=True, related_name='saved_by')

    # Profile status
    profile_completed = models.BooleanField(default=False)

    def bmi(self):
        if self.height_cm and self.weight_kg:
            h = self.height_cm / 100
            return round(self.weight_kg / (h * h), 1)
        return None

    def bmi_category(self):
        bmi = self.bmi()
        if bmi is None: return 'Unknown'
        if bmi < 18.5: return 'Underweight'
        elif bmi < 25: return 'Normal'
        elif bmi < 30: return 'Overweight'
        return 'Obese'

    def age(self):
        if self.date_of_birth:
            from datetime import date
            today = date.today()
            return today.year - self.date_of_birth.year
        return None
