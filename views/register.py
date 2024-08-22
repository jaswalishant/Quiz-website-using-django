from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from home.models import UserScore

#  code for register user
def register_user(request):
    if request.method=='POST':
        user_name=request.POST.get('name')
        passwd1=request.POST.get('passwd1')
        passwd2=request.POST.get('passwd2')
        
        exist=User.objects.filter(username=user_name).count()  # checking existing user
        if exist==0:
            if passwd1==passwd2:
                user_entry=User.objects.create_user(username=user_name, password=passwd1)  # creating user
                user_entry.save()

                # inserting same user in UserScore table
                if user_entry:
                    user=User.objects.get(username=user_name)
                    user_entry2=UserScore.objects.create(usern=user_name, user=user)
                    user_entry2.save()
                return redirect('login_user')
            else:
                content={
                    "msg":"The Password does not match",
                }
                return render(request, "register.html", content)
        else:
            content={
                "msg":"Username already exists"
            }
            return render(request, 'register.html', content)
    return render(request, "register.html")

