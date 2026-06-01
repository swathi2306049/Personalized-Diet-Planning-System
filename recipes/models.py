from django.db import models

class Recipe(models.Model):
    SEASON_CHOICES = [
        ('all', 'All Seasons'),
        ('summer', 'Summer'),
        ('winter', 'Winter'),
        ('monsoon', 'Monsoon'),
        ('spring', 'Spring'),
    ]
    MEAL_CHOICES = [
        ('breakfast', 'Breakfast'),
        ('lunch', 'Lunch'),
        ('dinner', 'Dinner'),
        ('snack', 'Snack'),
        ('drink', 'Drink'),
        ('dessert', 'Dessert'),
    ]
    DIET_CHOICES = [
        ('veg', 'Vegetarian'),
        ('non_veg', 'Non-Vegetarian'),
        ('vegan', 'Vegan'),
        ('eggetarian', 'Eggetarian'),
    ]
    HEALTH_CHOICES = [
        ('all', 'All'),
        ('diabetes', 'Diabetes Friendly'),
        ('hypertension', 'BP Friendly'),
        ('thyroid', 'Thyroid Friendly'),
        ('pcod', 'PCOD/PCOS Friendly'),
        ('weight_loss', 'Weight Loss'),
        ('weight_gain', 'Weight Gain'),
        ('heart', 'Heart Healthy'),
        ('cholesterol', 'Low Cholesterol'),
        ('anemia', 'Anemia Friendly'),
        ('gym', 'Gym / High Protein'),
        ('general', 'General Healthy'),
    ]

    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='recipes/', blank=True, null=True)
    image_url = models.CharField(max_length=500, blank=True, default='')
    description = models.TextField()
    ingredients = models.TextField()
    method = models.TextField()
    prep_time_min = models.IntegerField(default=10)
    cook_time_min = models.IntegerField(default=20)
    servings = models.IntegerField(default=2)
    meal_type = models.CharField(max_length=20, choices=MEAL_CHOICES)
    diet_type = models.CharField(max_length=20, choices=DIET_CHOICES)
    season = models.CharField(max_length=20, choices=SEASON_CHOICES, default='all')
    health_tags = models.CharField(max_length=50, choices=HEALTH_CHOICES)
    suitable_for = models.TextField(blank=True)
    avoid_for = models.TextField(blank=True)
    calories = models.IntegerField(default=0)
    protein_g = models.FloatField(default=0)
    carbs_g = models.FloatField(default=0)
    fat_g = models.FloatField(default=0)
    fiber_g = models.FloatField(default=0)
    sugar_g = models.FloatField(default=0)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def total_time(self):
        return self.prep_time_min + self.cook_time_min

    def get_image(self):
        if self.image:
            return self.image.url
        if self.image_url:
            return self.image_url
        return '/static/images/recipes/default.jpg'

    def __str__(self):
        return self.title