import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from website.models import ContactUs, Quote


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def home(request):
    if request.method == 'POST':
        mydata = json.loads(request.body)
        model = ContactUs(
            name=mydata['name'],
            email=mydata['email'],
            subject=mydata['subject'],
            message=mydata['message'],
        )
        model.save()
        return JsonResponse({'status': '200'})
    return render(request, 'home.html')


def get_a_quote(request):
    if request.method == 'POST':
        mydata = json.loads(request.body)
        model = Quote(
            name=mydata['quote_name'],
            email=mydata['quote_email'],
            service=mydata['quote_service'],
            budget=mydata['quote_budget'],
            phone=mydata['quote_phone'],
            company_name=mydata['quote_company_name'],
            message=mydata['quote_message'],
        )
        model.save()
        return JsonResponse({'status': '200'})
    return render(request, 'get_a_quote.html')

