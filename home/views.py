from django.shortcuts import render, redirect
# from django.contrib.auth.models import User
from home.models import UserScore, Gk, Computer, Animal, Sport, Science

# Create your views here.



# code for entering data (questions and options) according to different quizes
# def entry(request):
#     if request.method=="POST":
#         question=request.POST.get("question")
#         correct=request.POST.get("correct")
#         incorrect1=request.POST.get("incorrect1")
#         incorrect2=request.POST.get("incorrect2")
#         incorrect3=request.POST.get("incorrect3")

#         enter=Sport.objects.create(question=question, correct=correct ,incorrect1=incorrect1 , incorrect2=incorrect2, incorrect3=incorrect3)
#         enter.save()

#     return render(request, "entry.html")