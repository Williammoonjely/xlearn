from django.shortcuts import render
from accounts.forms import Signin
from django.contrib.auth import login,authenticate,logout

# Create your views here.

def spot(request):
    if request.method == "POST":
        signin_form = Signin(request.POST)
        if signin_form.is_valid():
            cd = signin_form.cleaned_data
            print(cd)
            user_name = cd['user_name']
            passwor = cd['user_password']
            user = authenticate(request,username=user_name,password=passwor)
            if user is not None:
                login(request,user)
                return render(request,'dash/dash.html')
                print('you are login')
            else:
                print('incorrect login')
 
    
    login_form = Signin()
    context = {
        'signin_form':login_form
    }
    return render(request,'core/spot.html',context)