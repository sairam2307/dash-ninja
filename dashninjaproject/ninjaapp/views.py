from django.shortcuts import render,redirect
from ninjaapp.models import *


def tab(request):
    categories = Category.objects.filter(status=True)
    footer_items = Footer.objects.filter(status=True)
    company_item = Company.objects.filter(status=True).last()

    return render(request, 'tab.html',{'categories':categories,'footer_items':footer_items,'company_item':company_item})