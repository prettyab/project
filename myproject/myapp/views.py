

# Create your views here.
# employee/views.py

from django.shortcuts import render, redirect

def registration_view(request):
    if request.method == 'POST':
        # Handle form submission logic here (e.g., create a new employee record)
        # After successful registration, redirect to the login page
        return redirect('login')
    else:
        return render(request, 'register.html')

def login_view(request):
    # Your login view logic here
    return render(request, 'loggin.html')

