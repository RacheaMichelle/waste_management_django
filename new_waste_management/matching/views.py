from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from users.models import Profile
from waste.models import WasteListing
from .models import Notification
from django.utils import timezone
from django.core.paginator import Paginator

@login_required
def matches(request):
    user_profile = request.user.profile
    matches = []
    new_notifications = False

    if user_profile.user_type in ['household', 'business']:
        listings = WasteListing.objects.filter(user=request.user).select_related('user')
        
        for listing in listings:
            # Ensure both collectors and recyclers are included
            collectors = Profile.objects.filter(
                user_type__in=['collector', 'recycler'],  # Explicitly includes both
                accepted_waste_types__contains=listing.waste_type,
                location=user_profile.location
            ).exclude(contact__isnull=True).exclude(contact__exact='')
            
            # Create notifications for new matches
            for collector in collectors:
                if not Notification.objects.filter(
                    recipient=request.user,
                    listing=listing,
                    message__contains=collector.user.username
                ).exists():
                    Notification.objects.create(
                        recipient=request.user,
                        listing=listing,
                        message=f"New match! {collector.user.username} ({collector.get_user_type_display()}) can collect your {listing.waste_type} waste."
                    )
                    new_notifications = True

            matches.append({
                'listing': listing,
                'collectors': collectors,  # Should include both collectors and recyclers
            })

    elif user_profile.user_type in ['collector', 'recycler']:
        accepted_types = user_profile.accepted_waste_types.split(',')
        listings = WasteListing.objects.filter(
            waste_type__in=accepted_types,
            location=user_profile.location
        ).exclude(user=request.user)
        
        for listing in listings:
            listing_owner = Profile.objects.get(user=listing.user)
            
            if not Notification.objects.filter(
                recipient=request.user,
                listing=listing,
                message__contains=listing.user.username
            ).exists():
                Notification.objects.create(
                    recipient=request.user,
                    listing=listing,
                    message=f"New listing! {listing.user.username} has {listing.quantity}kg of {listing.waste_type} in {listing.location}."
                )
                new_notifications = True
            
            matches.append({
                'listing': listing,
                'listing_owner': listing_owner,
            })

    if new_notifications:
        messages.info(request, "You have new matches!")

    return render(request, 'matching/matches.html', {
        'matches': matches,
        'user_profile': user_profile
    })

@login_required
def notifications(request):
    notifications = Notification.objects.filter(
        recipient=request.user
    ).order_by('-created_at').select_related('listing', 'recipient')
    
    # Paginate notifications (10 per page)
    paginator = Paginator(notifications, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    unread_notifications = notifications.filter(is_read=False)
    if unread_notifications.exists():
        unread_notifications.update(is_read=True)
        messages.success(request, f"You have {unread_notifications.count()} new notifications")
    
    return render(request, 'matching/notifications.html', {
        'page_obj': page_obj,
        'notifications': page_obj.object_list
    })

@login_required
def mark_notification_read(request, notification_id):
    notification = Notification.objects.get(id=notification_id, recipient=request.user)
    notification.is_read = True
    notification.save()
    return redirect(request.META.get('HTTP_REFERER', 'notifications'))

@login_required
def delete_notification(request, notification_id):
    notification = Notification.objects.get(id=notification_id, recipient=request.user)
    notification.delete()
    messages.success(request, "Notification deleted successfully.")
    return redirect(request.META.get('HTTP_REFERER', 'notifications'))

@login_required
def clear_all_notifications(request):
    Notification.objects.filter(recipient=request.user).delete()
    messages.success(request, "All notifications have been cleared.")
    return redirect('notifications')