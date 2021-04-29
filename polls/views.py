from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from polls.models import index
from django.contrib import messages
import csv
# Create your views here.
def formss(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        profession = request.POST.get('profession')
        formss = index(name=name, email=email, phone=phone, address=address, profession=profession, date=datetime.today())
        formss.save()
        messages.success(request, "Your form has been submitted succesfully")
    #return HttpResponse("hello world, you're at polls index.")
    return render(request, 'formss.html')

def home(request):
    return render(request, 'home.html')

def export_formss(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="forms.csv"'

    writer = csv.writer(response)
    writer.writerow(['Name', 'Email','Phone no.', 'Address', 'Profession', 'Date of filling'])

    application = index.objects.all().values_list('name', 'email', 'phone', 'address', 'profession', 'date')
    for form_app in application:
        writer.writerow(form_app)
    
    return response