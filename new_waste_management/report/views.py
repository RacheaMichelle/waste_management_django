from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import DumpingReportForm
from .models import DumpingReport
from .district_contacts import get_district_contact

def report_dumping(request):
    if request.method == 'POST':
        form = DumpingReportForm(request.POST, request.FILES)
        if form.is_valid():
            report = form.save()
            
            district_number = get_district_contact(report.district)
            sms_content = (
                f"New dumping report in {report.district}\n"
                f"Type: {report.get_waste_type_display()}\n"
                f"Location: {report.latitude}, {report.longitude}"
            )
            print(f"\nSMS would be sent to {district_number}:\n{sms_content}\n")

            messages.success(request, "Report submitted! Authorities will be notified.")
            return redirect('report_success', report_id=report.id)
    else:
        form = DumpingReportForm()
    return render(request, 'report/report_form.html', {'form': form})


# ✅ Add this below the existing view
def report_success(request, report_id):
    return render(request, 'report/report_success.html', {'report_id': report_id})
