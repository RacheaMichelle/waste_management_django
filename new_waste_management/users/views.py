from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from .models import Profile
from .forms import QuickRegisterForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user_type = form.cleaned_data['user_type']
            location = form.cleaned_data['location']
            contact = form.cleaned_data['contact']
            accepted_waste_types = ','.join(form.cleaned_data.get('accepted_waste_types', []))
            profile = Profile(
                user=user,
                user_type=user_type,
                location=location,
                contact=contact,
                accepted_waste_types=accepted_waste_types
            )
            profile.save()
            login(request, user)
            return redirect('/')  # Temporary redirect to root
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})
@login_required
def profile(request):
    is_quick_access = False
    try:
        if request.user.profile.user_type == 'quick_access':
            is_quick_access = True
    except Profile.DoesNotExist:
        pass

    return render(request, 'users/profile.html', {
        'profile': request.user.profile,
        'is_quick_access': is_quick_access,
    })

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()

        if not username or not password:
            return render(request, 'users/login.html', {'error': 'Username and password are required.'})

        user = authenticate(request, username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)

                # Redirect quick access users to their dashboard
                try:
                    if user.profile.user_type == 'quick_access':
                        return redirect('quick_dashboard')
                except Profile.DoesNotExist:
                    pass  # No profile; proceed to next_url or default

                # Continue with normal redirect
                next_url = request.GET.get('next', '/')
                return redirect(next_url)
            else:
                return render(request, 'users/login.html', {'error': 'Account is disabled.'})
        else:
            return render(request, 'users/login.html', {'error': 'Invalid credentials'})

    else:
        next_url = request.GET.get('next', '/')
        return render(request, 'users/login.html', {'next': next_url})

def user_logout(request):
    logout(request)
    return redirect('home')  # Ensure 'home' is defined in URLs


def quick_register(request):
    if request.method == 'POST':
        form = QuickRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)

            # Redirect to quick dashboard for quick access users
            return redirect('quick_dashboard')
    else:
        form = QuickRegisterForm()
    return render(request, 'users/quick_register.html', {'form': form})

@login_required
def quick_dashboard(request):
    # For quick dashboard, user is definitely quick_access, but check anyway
    is_quick_access = False
    try:
        if request.user.profile.user_type == 'quick_access':
            is_quick_access = True
    except Profile.DoesNotExist:
        pass

    return render(request, 'users/quick_dashboard.html', {
        'is_quick_access': is_quick_access,
    })
