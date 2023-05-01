from django.shortcuts import *
from .forms import *

# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def account(request):
    return render(request, 'main/account.html')

def about(request):
    return render(request, 'main/about.html')

def contact(request):
    return render(request, 'main/contact.html')

def reg(request):
    form = ClientForm(request.POST or None)
    if request.method == 'POST':
        print(request.POST)
        new_form = form.save()

    return render(request, 'main/reg.html', locals())
    # form = ClientForm(request.POST or None)
    # if request.method == 'POST':
    #     return redirect("account")
    # data = {
    #     "form": ClientForm(),
    # }
    # return render(request, 'main/reg.html', data)

def entrance(request):
    q = "ghghgh"
    if request.method == "POST":
        form = ClientForm(request.POST)
        return redirect("account")
    data = {
        "form": ClientForm(),
    }
    return render(request, 'main/entrance.html', data)



