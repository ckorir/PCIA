from django.shortcuts import render
from django.http  import HttpResponse, Http404, HttpResponseRedirect
from .forms import InquiryForm
from .models import Inquiry

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
            subject = form.cleaned_data['subject']
            location = form.cleaned_data['location']
            cover_type = form.cleaned_data['cover_type']
            message = form.cleaned_data['message']
            question = Inquiry(first_name = first_name,last_name = last_name,phone_number = phone_number,email =email, subject = subject, location = location, cover_type = cover_type, message = message)
            question.save()
            HttpResponseRedirect('inquiry')
    else:
        form = InquiryForm()
    return render(request, 'inquiry.html', {"letterForm":form})