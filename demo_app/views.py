from django.shortcuts import render , redirect
from .forms import InputForm
from .models import Customers

# Create your views here.
def index(request):
#    return render(request, 'demo_app/index.html', {})
    if request.method == 'POST':
        if "to_input" in request.POST:
            input_form()
    else:
         return render(request, 'demo_app/index.html', {})

def input_form(request):
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            form.save() # 入力された値を保存
            return redirect('result')
    else:
        form = InputForm()
        return render(request,'demo_app/input_form.html',{'form':form})


def result(request):
    return render(request , 'demo_app/result.html', {})
