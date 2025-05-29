from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from datetime import timedelta
from waste.models import WasteListing
from matching.models import Notification
from education.models import Resource
from analytics.models import ResourceView
from collections import defaultdict

@login_required
def analytics(request):
    user_profile = request.user.profile
    today = timezone.now()
    default_start_date = today - timedelta(days=30)
    start_date = request.GET.get('start_date', default_start_date.strftime('%Y-%m-%d'))
    end_date = request.GET.get('end_date', today.strftime('%Y-%m-%d'))

    # Convert to datetime objects
    start_date = timezone.datetime.strptime(start_date, '%Y-%m-%d').replace(tzinfo=timezone.get_current_timezone())
    end_date = timezone.datetime.strptime(end_date, '%Y-%m-%d').replace(tzinfo=timezone.get_current_timezone()) + timedelta(days=1)

    # Initialize data structures
    quantity_by_type_unit = defaultdict(lambda: defaultdict(float))
    listing_owners = defaultdict(set)
    listings_by_type = defaultdict(int)
    waste_types = set()

    # User-specific stats
    if user_profile.user_type in ['household', 'business']:
        listings = WasteListing.objects.filter(
            user=request.user,
            created_at__range=(start_date, end_date)
        ).select_related('user')
        
        for listing in listings:
            # Process quantity
            if listing.quantity:
                try:
                    quantity_str = str(listing.quantity).strip()
                    parts = quantity_str.split()
                    if parts and parts[0].replace('.', '').isdigit():
                        number = float(parts[0])
                        unit = ' '.join(parts[1:]).lower() if len(parts) > 1 else 'kg'
                        quantity_by_type_unit[listing.waste_type][unit] += number
                except (ValueError, IndexError):
                    pass
            
            # Count listings by type
            listings_by_type[listing.waste_type] += 1
            waste_types.add(listing.waste_type)

    elif user_profile.user_type in ['collector', 'recycler']:
        accepted_types = [t.strip() for t in user_profile.accepted_waste_types.split(',') if t.strip()]
        listings = WasteListing.objects.filter(
            waste_type__in=accepted_types,
            location=user_profile.location,
            created_at__range=(start_date, end_date)
        ).select_related('user')
        
        for listing in listings:
            # Process quantity
            if listing.quantity:
                try:
                    quantity_str = str(listing.quantity).strip()
                    parts = quantity_str.split()
                    if parts and parts[0].replace('.', '').isdigit():
                        number = float(parts[0])
                        unit = ' '.join(parts[1:]).lower() if len(parts) > 1 else 'kg'
                        quantity_by_type_unit[listing.waste_type][unit] += number
                except (ValueError, IndexError):
                    pass
            
            # Track owners and count listings
            listing_owners[listing.waste_type].add(listing.user.username)
            listings_by_type[listing.waste_type] += 1
            waste_types.add(listing.waste_type)

    # Convert defaultdicts to regular dicts for template
    quantity_by_type_unit = {k: dict(v) for k, v in quantity_by_type_unit.items()}
    listing_owners = {k: list(v) for k, v in listing_owners.items()}
    
    # Other metrics
    total_listings = sum(listings_by_type.values())
    matches = Notification.objects.filter(
        recipient=request.user,
        created_at__range=(start_date, end_date)
    ).count()
    resource_views = ResourceView.objects.filter(
        user=request.user,
        viewed_at__range=(start_date, end_date)
    ).count()

    # Products made from relevant waste types
    products_made = {
        resource.waste_type: resource.products_made 
        for resource in Resource.objects.filter(waste_type__in=waste_types)
    }

    context = {
        'total_listings': total_listings,
        'quantity_by_type_unit': quantity_by_type_unit,
        'listing_owners': listing_owners,
        'matches': matches,
        'resource_views': resource_views,
        'products_made': products_made,
        'chart_labels': list(listings_by_type.keys()),
        'chart_data': list(listings_by_type.values()),
        'start_date': start_date.strftime('%Y-%m-%d'),
        'end_date': (end_date - timedelta(days=1)).strftime('%Y-%m-%d'),  # Subtract the extra day we added
    }
    return render(request, 'analytics/dashboard.html', context)