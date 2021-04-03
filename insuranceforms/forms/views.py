from django.shortcuts import render
from django.http  import HttpResponse, Http404, HttpResponseRedirect
from .forms import InquiryForm, PrivateForm, PSVForm, CommercialForm
from .models import Inquiry, PrivateMotor, PSV, CommercialVehicle
from django.contrib import messages

# Create your views here.
def welcome(request):
    return render(request, 'index.html')

def inquiry(request):
    if request.method == 'POST':
        form = InquiryForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            location = form.cleaned_data['location']
            cover_type = form.cleaned_data['cover_type']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            question = Inquiry(first_name = first_name,last_name = last_name,phone_number = phone_number,email =email, location = location, cover_type = cover_type, subject = subject, message = message)
            question.save()
            messages.success(request, 'Inquiry Submission Successful')
            form = InquiryForm()
    else:
        form = InquiryForm()
    return render(request, 'inquiry.html', {"letterForm":form})

def privatemotor(request):
    if request.method == 'POST':
        form = PrivateForm(request.POST)
        if form.is_valid():
            cover_type = form.cleaned_data['cover_type']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            vehicle_make = form.cleaned_data['vehicle_make']
            vehicle_model = form.cleaned_data['vehicle_model']
            registration_number = form.cleaned_data['registration_number']
            YOM = form.cleaned_data['YOM']
            color = form.cleaned_data['color']
            period_from = form.cleaned_data['period_from']
            period_to = form.cleaned_data['period_to']
            private = PrivateMotor(cover_type = cover_type,first_name = first_name,last_name = last_name,phone_number = phone_number,email =email, vehicle_make = vehicle_make, vehicle_model = vehicle_model, registration_number = registration_number, YOM = YOM, color = color, period_from = period_from, period_to = period_to)
            private.save()
            messages.success(request, 'Private Motor Quotation Inquiry Submission Successful')
            form = PrivateForm()
    else:
        form = PrivateForm()
    return render(request, 'privatemotor.html', {"letterForm":form})

def psv(request):
    if request.method == 'POST':
        form = PSVForm(request.POST)
        if form.is_valid():
            cover_type = form.cleaned_data['cover_type']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            vehicle_make = form.cleaned_data['vehicle_make']
            vehicle_model = form.cleaned_data['vehicle_model']
            passengers = form.cleaned_data['passengers']
            registration_number = form.cleaned_data['registration_number']
            YOM = form.cleaned_data['YOM']
            color = form.cleaned_data['color']
            period_from = form.cleaned_data['period_from']
            period_to = form.cleaned_data['period_to']
            bus = PSV(cover_type = cover_type,first_name = first_name,last_name = last_name,phone_number = phone_number,email =email, vehicle_make = vehicle_make, vehicle_model = vehicle_model, passengers = passengers, registration_number = registration_number, YOM = YOM, color = color, period_from = period_from, period_to = period_to)
            bus.save()
            messages.success(request, 'PSV Quotation Inquiry Submission Successful')
            form = PSVForm()
    else:
        form = PSVForm()
    return render(request, 'psv.html', {"letterForm":form})

def commercial(request):
    if request.method == 'POST':
        form = CommercialForm(request.POST)
        if form.is_valid():
            cover_type = form.cleaned_data['cover_type']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            vehicle_make = form.cleaned_data['vehicle_make']
            vehicle_model = form.cleaned_data['vehicle_model']
            registration_number = form.cleaned_data['registration_number']
            YOM = form.cleaned_data['YOM']
            color = form.cleaned_data['color']
            period_from = form.cleaned_data['period_from']
            period_to = form.cleaned_data['period_to']
            comm = CommercialVehicle(cover_type = cover_type,first_name = first_name,last_name = last_name,phone_number = phone_number,email =email, vehicle_make = vehicle_make, vehicle_model = vehicle_model, registration_number = registration_number, YOM = YOM, color = color, period_from = period_from, period_to = period_to)
            comm.save()
            messages.success(request, 'Commercial Vehicle Quotation Inquiry Submission Successful')
            form = CommercialForm()
    else:
        form = CommercialForm()
    return render(request, 'commercial.html', {"letterForm":form})