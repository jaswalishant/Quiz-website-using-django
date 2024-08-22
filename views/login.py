from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

# code for login user
def login_user(request):
    if request.method=='POST':
        user_name=request.POST.get('name')
        passwd=request.POST.get('password')

        # authenticating user according to username and password
        user=authenticate(request, username=user_name, password=passwd)
        if user is not None:
            login(request,user)
            request.session["user_name"]=user_name
            return redirect("dashboard")
        else:
            content={
                "msg":"Wrong Password, Try again"
            }
            return render(request, "login.html", content)
    return render(request, "login.html")



# code for logging out user
def logout_user(request):
    logout(request)
    return redirect('login_user')

