def quick_access_status(request):
    is_quick_access = False
    if request.user.is_authenticated:
        try:
            if request.user.profile.user_type == 'quick_access':
                is_quick_access = True
        except Exception:
            pass
    return {
        'is_quick_access': is_quick_access,
    }
