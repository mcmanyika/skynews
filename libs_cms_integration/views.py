from django.shortcuts import render
from .models import acct

# Create your views here.


def accts(request):
    acct = acct.objects.all()
    render(request, 'libs_cms_integration/libs_plugin.html', {"acct": acct})
