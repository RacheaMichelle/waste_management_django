from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import WasteListingForm
from .models import WasteListing

@login_required
def list_waste(request):
    if request.method == 'POST':
        form = WasteListingForm(request.POST, request.FILES)
        if form.is_valid():
            listing = form.save(commit=False)
            listing.user = request.user
            listing.save()
            return redirect('waste_list')
    else:
        form = WasteListingForm()
    listings = WasteListing.objects.filter(user=request.user)
    return render(request, 'waste/list.html', {'form': form, 'listings': listings})