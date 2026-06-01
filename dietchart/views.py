from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .algorithm import generate_diet_chart

@login_required
def diet_chart_view(request):
    user = request.user
    if not user.profile_completed:
        messages.warning(request, 'Complete your profile first!')
        return redirect('profile')
    if not user.weight_kg or not user.height_cm:
        messages.warning(request, 'Add height and weight in profile!')
        return redirect('profile')
    chart_data = generate_diet_chart(user)
    return render(request, 'dietchart/dietchart.html', {
        'chart': chart_data, 'user': user
    })
