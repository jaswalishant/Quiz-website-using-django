from django.shortcuts import render
from views.dashboard import returning_lists

questions_list= returning_lists()[0]
correct_answers= returning_lists()[2]
# code for displaying correct answers
def check_answers(request):
    numbers=list(range(0,len(questions_list)))
    if request.method=="POST":
        content={
            "question":questions_list,
            "answer":correct_answers,
            "numbers":numbers,
        }
        return render(request, "correct.html", content)
    return render(request, "correct.html")

