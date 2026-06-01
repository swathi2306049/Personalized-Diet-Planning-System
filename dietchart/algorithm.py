# dietchart/algorithm.py

DAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# ===== WEIGHT LOSS FOODS =====
WEIGHT_LOSS_BREAKFAST = [
    {'name': 'Oats Porridge with Berries', 'calories': 280, 'protein': 10, 'carbs': 45, 'fat': 6},
    {'name': 'Moong Dal Chilla + Mint Chutney', 'calories': 220, 'protein': 12, 'carbs': 30, 'fat': 5},
    {'name': 'Poha with Vegetables', 'calories': 250, 'protein': 8, 'carbs': 40, 'fat': 5},
    {'name': 'Idli Sambar (3 pieces)', 'calories': 200, 'protein': 8, 'carbs': 38, 'fat': 3},
    {'name': 'Vegetable Upma', 'calories': 230, 'protein': 7, 'carbs': 38, 'fat': 6},
    {'name': 'Egg White Omelette with Veggies', 'calories': 180, 'protein': 18, 'carbs': 5, 'fat': 6},
    {'name': 'Greek Yogurt with Flaxseeds', 'calories': 200, 'protein': 15, 'carbs': 20, 'fat': 5},
]

WEIGHT_LOSS_LUNCH = [
    {'name': 'Brown Rice + Dal + Salad', 'calories': 350, 'protein': 15, 'carbs': 55, 'fat': 6},
    {'name': 'Ragi Roti + Palak Sabzi + Raita', 'calories': 320, 'protein': 12, 'carbs': 50, 'fat': 7},
    {'name': 'Quinoa Vegetable Bowl', 'calories': 300, 'protein': 14, 'carbs': 45, 'fat': 7},
    {'name': 'Grilled Chicken Salad', 'calories': 280, 'protein': 35, 'carbs': 15, 'fat': 8},
    {'name': 'Wheat Roti + Mixed Veg Curry', 'calories': 340, 'protein': 12, 'carbs': 52, 'fat': 8},
    {'name': 'Dal Khichdi with Curd', 'calories': 310, 'protein': 13, 'carbs': 50, 'fat': 6},
    {'name': 'Steamed Fish + Brown Rice', 'calories': 290, 'protein': 32, 'carbs': 35, 'fat': 5},
]

WEIGHT_LOSS_DINNER = [
    {'name': 'Vegetable Soup + 2 Wheat Roti', 'calories': 250, 'protein': 10, 'carbs': 38, 'fat': 5},
    {'name': 'Paneer Tikka + Green Salad', 'calories': 280, 'protein': 18, 'carbs': 12, 'fat': 15},
    {'name': 'Moong Dal Soup + Roti', 'calories': 240, 'protein': 14, 'carbs': 36, 'fat': 4},
    {'name': 'Grilled Chicken + Stir-fry Veggies', 'calories': 260, 'protein': 30, 'carbs': 15, 'fat': 8},
    {'name': 'Lentil Soup + Brown Bread', 'calories': 230, 'protein': 12, 'carbs': 35, 'fat': 4},
    {'name': 'Tofu Stir Fry with Vegetables', 'calories': 220, 'protein': 16, 'carbs': 18, 'fat': 10},
    {'name': 'Mixed Veg Daliya', 'calories': 200, 'protein': 9, 'carbs': 32, 'fat': 4},
]

# ===== WEIGHT GAIN FOODS =====
WEIGHT_GAIN_BREAKFAST = [
    {'name': 'Banana Peanut Butter Oats', 'calories': 480, 'protein': 18, 'carbs': 65, 'fat': 16},
    {'name': 'Whole Egg Omelette + Whole Wheat Toast', 'calories': 450, 'protein': 25, 'carbs': 40, 'fat': 20},
    {'name': 'Paneer Paratha with Curd (2 pcs)', 'calories': 500, 'protein': 20, 'carbs': 55, 'fat': 22},
    {'name': 'Dry Fruits Milk Shake + Poha', 'calories': 520, 'protein': 16, 'carbs': 70, 'fat': 18},
    {'name': 'Peanut Butter Banana Smoothie', 'calories': 460, 'protein': 20, 'carbs': 58, 'fat': 16},
    {'name': 'Chicken Sandwich + Boiled Eggs', 'calories': 500, 'protein': 35, 'carbs': 42, 'fat': 18},
    {'name': 'Masala Dosa + Sambar + Coconut Chutney', 'calories': 440, 'protein': 14, 'carbs': 65, 'fat': 15},
]

WEIGHT_GAIN_LUNCH = [
    {'name': 'White Rice + Rajma + Roti + Curd', 'calories': 600, 'protein': 22, 'carbs': 90, 'fat': 12},
    {'name': 'Chicken Biryani with Raita', 'calories': 650, 'protein': 38, 'carbs': 75, 'fat': 18},
    {'name': 'Paneer Butter Masala + Naan', 'calories': 620, 'protein': 24, 'carbs': 72, 'fat': 25},
    {'name': 'Mutton Curry + Rice + Dal', 'calories': 680, 'protein': 45, 'carbs': 70, 'fat': 22},
    {'name': 'Chole Bhature', 'calories': 580, 'protein': 18, 'carbs': 80, 'fat': 20},
    {'name': 'Egg Fried Rice + Manchurian', 'calories': 560, 'protein': 22, 'carbs': 82, 'fat': 15},
    {'name': 'Soya Chunks Curry + Rice + Roti', 'calories': 600, 'protein': 40, 'carbs': 70, 'fat': 12},
]

WEIGHT_GAIN_DINNER = [
    {'name': 'Palak Paneer + 3 Rotis + Rice', 'calories': 520, 'protein': 22, 'carbs': 68, 'fat': 18},
    {'name': 'Fish Curry + Rice + Salad', 'calories': 500, 'protein': 40, 'carbs': 55, 'fat': 14},
    {'name': 'Dal Makhani + Roti + Rice', 'calories': 480, 'protein': 18, 'carbs': 65, 'fat': 16},
    {'name': 'Chicken Stew + Appam', 'calories': 510, 'protein': 35, 'carbs': 58, 'fat': 14},
    {'name': 'Paneer Paratha + Raita + Salad', 'calories': 490, 'protein': 20, 'carbs': 60, 'fat': 18},
    {'name': 'Egg Curry + Brown Rice', 'calories': 470, 'protein': 28, 'carbs': 55, 'fat': 16},
    {'name': 'Tofu Palak + Quinoa', 'calories': 450, 'protein': 25, 'carbs': 48, 'fat': 15},
]

# ===== BALANCED DIET FOODS =====
BALANCED_BREAKFAST = [
    {'name': 'Oats with Fruits and Nuts', 'calories': 350, 'protein': 12, 'carbs': 55, 'fat': 10},
    {'name': 'Idli Sambar (4 pieces)', 'calories': 300, 'protein': 10, 'carbs': 55, 'fat': 4},
    {'name': 'Upma with Veggies + Tea', 'calories': 320, 'protein': 9, 'carbs': 50, 'fat': 8},
    {'name': 'Whole Wheat Toast + Boiled Egg + Juice', 'calories': 340, 'protein': 18, 'carbs': 42, 'fat': 10},
    {'name': 'Dosa with Coconut Chutney', 'calories': 280, 'protein': 8, 'carbs': 48, 'fat': 8},
    {'name': 'Poha with Sprouts', 'calories': 300, 'protein': 12, 'carbs': 45, 'fat': 6},
    {'name': 'Smoothie Bowl with Granola', 'calories': 360, 'protein': 14, 'carbs': 52, 'fat': 10},
]

BALANCED_LUNCH = [
    {'name': 'Roti + Dal + Sabzi + Salad', 'calories': 420, 'protein': 16, 'carbs': 62, 'fat': 10},
    {'name': 'Brown Rice + Rajma + Curd', 'calories': 400, 'protein': 18, 'carbs': 60, 'fat': 8},
    {'name': 'Mixed Veg Pulao + Raita', 'calories': 390, 'protein': 12, 'carbs': 58, 'fat': 10},
    {'name': 'Chapati + Chicken Curry + Salad', 'calories': 430, 'protein': 28, 'carbs': 52, 'fat': 12},
    {'name': 'Wheat Roti + Paneer Sabzi + Dal', 'calories': 410, 'protein': 20, 'carbs': 55, 'fat': 12},
    {'name': 'Sambar Rice + Papad', 'calories': 380, 'protein': 14, 'carbs': 60, 'fat': 7},
    {'name': 'Millet Khichdi + Curd', 'calories': 370, 'protein': 14, 'carbs': 55, 'fat': 8},
]

BALANCED_DINNER = [
    {'name': '2 Rotis + Sabzi + Dal', 'calories': 380, 'protein': 14, 'carbs': 58, 'fat': 9},
    {'name': 'Rice + Lentil Curry', 'calories': 360, 'protein': 15, 'carbs': 55, 'fat': 8},
    {'name': 'Grilled Fish + Roti + Salad', 'calories': 350, 'protein': 32, 'carbs': 36, 'fat': 10},
    {'name': 'Paneer Bhurji + 2 Rotis', 'calories': 370, 'protein': 20, 'carbs': 38, 'fat': 16},
    {'name': 'Veg Khichdi + Buttermilk', 'calories': 330, 'protein': 12, 'carbs': 52, 'fat': 8},
    {'name': 'Chicken Soup + Wheat Bread', 'calories': 340, 'protein': 25, 'carbs': 38, 'fat': 9},
    {'name': 'Mixed Dal + Roti + Stir-fry Veggies', 'calories': 350, 'protein': 16, 'carbs': 50, 'fat': 8},
]

# ===== PHYSICAL ACTIVITIES =====
PHYSICAL_ACTIVITIES = {
    'weight_loss': [
        '30 min brisk walking daily',
        '20 min cycling or swimming',
        '15 min HIIT workout',
        'Yoga — Surya Namaskar 12 rounds',
        'Zumba or aerobics for 30 min',
        'Jump rope for 15 min',
        'Jogging 3-4 km',
    ],
    'weight_gain': [
        'Strength training — upper body (chest, shoulders, arms)',
        'Strength training — lower body (squats, lunges)',
        'Deadlifts and squats — 3 sets each',
        'Pull-ups and push-ups — 4 sets each',
        'Bench press and shoulder press',
        'Leg press and leg curls',
        'Core strengthening — planks and crunches',
    ],
    'balanced': [
        '30 min morning walk',
        '15 min stretching and yoga',
        '20 min light jog',
        'Swimming for 30 min',
        'Cycling for 30 min',
        'Bodyweight exercises — 20 min',
        'Meditation and Pranayama — 20 min',
    ],
}


def calculate_bmi(weight_kg, height_cm):
    if not weight_kg or not height_cm:
        return None
    h = height_cm / 100
    return round(weight_kg / (h * h), 1)


def get_diet_category(bmi, goal, target_weight_kg, current_weight_kg):
    """
    Smart algorithm that considers both BMI and goal together.
    BMI categories:
      < 18.5  = Underweight
      18.5-24.9 = Normal
      25-29.9 = Overweight
      30+     = Obese
    """

    # ── CASE 1: No BMI data available ──────────────────────────────
    if bmi is None:
        if goal == 'weight_loss':
            return 'weight_loss'
        elif goal in ['weight_gain', 'muscle_gain']:
            return 'weight_gain'
        return 'balanced'

    # ── CASE 2: User is OBESE (BMI 30+) ────────────────────────────
    # Never recommend weight gain for obese users regardless of goal
    if bmi >= 30:
        return 'weight_loss'

    # ── CASE 3: User is OVERWEIGHT (BMI 25-29.9) ───────────────────
    if 25 <= bmi < 30:
        if goal == 'weight_loss':
            return 'weight_loss'
        elif goal in ['weight_gain', 'muscle_gain']:
            # Overweight person asking for weight gain
            # Check if target weight is also overweight range
            if target_weight_kg and current_weight_kg:
                if target_weight_kg > current_weight_kg:
                    # They want to gain MORE weight but already overweight
                    # Override to weight loss
                    return 'weight_loss_override'
                else:
                    return 'weight_loss'
            return 'weight_loss_override'
        elif goal == 'maintain':
            return 'balanced'
        elif goal == 'health_condition':
            return 'balanced'
        return 'weight_loss'

    # ── CASE 4: User is NORMAL weight (BMI 18.5-24.9) ──────────────
    if 18.5 <= bmi < 25:
        if goal == 'weight_loss':
            return 'weight_loss'
        elif goal in ['weight_gain', 'muscle_gain']:
            return 'weight_gain'
        elif goal == 'maintain':
            return 'balanced'
        return 'balanced'

    # ── CASE 5: User is UNDERWEIGHT (BMI < 18.5) ───────────────────
    if bmi < 18.5:
        if goal == 'weight_loss':
            # Underweight person asking to lose weight — dangerous
            # Override to balanced
            return 'underweight_override'
        elif goal in ['weight_gain', 'muscle_gain']:
            return 'weight_gain'
        return 'weight_gain'

    return 'balanced'


def generate_diet_chart(user):
    bmi = calculate_bmi(user.weight_kg, user.height_cm)
    category = get_diet_category(
        bmi,
        user.goal,
        user.target_weight_kg,
        user.weight_kg
    )

    # ── Select food lists based on category ─────────────────────────
    if category in ('weight_loss', 'weight_loss_override'):
        breakfasts = WEIGHT_LOSS_BREAKFAST
        lunches    = WEIGHT_LOSS_LUNCH
        dinners    = WEIGHT_LOSS_DINNER
        activities = PHYSICAL_ACTIVITIES['weight_loss']
        daily_calorie_target = '1200 - 1500 kcal'
        weekly_goal = '0.5 kg per week weight loss'

    elif category == 'weight_gain':
        breakfasts = WEIGHT_GAIN_BREAKFAST
        lunches    = WEIGHT_GAIN_LUNCH
        dinners    = WEIGHT_GAIN_DINNER
        activities = PHYSICAL_ACTIVITIES['weight_gain']
        daily_calorie_target = '2500 - 3000 kcal'
        weekly_goal = '0.5 kg per week weight gain'

    elif category in ('balanced', 'underweight_override'):
        breakfasts = BALANCED_BREAKFAST
        lunches    = BALANCED_LUNCH
        dinners    = BALANCED_DINNER
        activities = PHYSICAL_ACTIVITIES['balanced']
        daily_calorie_target = '1800 - 2200 kcal'
        weekly_goal = 'Maintain current weight'

    else:
        breakfasts = BALANCED_BREAKFAST
        lunches    = BALANCED_LUNCH
        dinners    = BALANCED_DINNER
        activities = PHYSICAL_ACTIVITIES['balanced']
        daily_calorie_target = '1800 - 2200 kcal'
        weekly_goal = 'Maintain current weight'

    # ── Build 7-day weekly chart ─────────────────────────────────────
    weekly_chart = []
    for i, day in enumerate(DAYS):
        breakfast = breakfasts[i % len(breakfasts)]
        lunch     = lunches[i % len(lunches)]
        dinner    = dinners[i % len(dinners)]
        activity  = activities[i % len(activities)]
        total_cal = (
            breakfast['calories'] +
            lunch['calories'] +
            dinner['calories'] + 220
        )
        weekly_chart.append({
            'day':            day,
            'breakfast':      breakfast,
            'lunch':          lunch,
            'dinner':         dinner,
            'activity':       activity,
            'total_calories': total_cal,
        })

    # ── Calculate weeks to reach target ─────────────────────────────
    weeks_to_target = None
    if user.target_weight_kg and user.weight_kg:
        gap = abs(user.target_weight_kg - user.weight_kg)
        if gap > 0:
            weeks_to_target = round(gap / 0.5)

    return {
        'weekly_chart':        weekly_chart,
        'bmi':                 bmi,
        'category':            category,
        'goal':                user.goal,
        'daily_calorie_target': daily_calorie_target,
        'weekly_goal':         weekly_goal,
        'weeks_to_target':     weeks_to_target,
    }