from django.shortcuts import render
from home.models import UserScore
from views.dashboard import returning_lists


correct_answers= returning_lists()[2]   # list for correct answers imported from dashboard.py file using index for returning values
# function for storing scores of the user
def storing_scores(user_name, table, correct):
    user=UserScore.objects.get(usern=user_name)

     # code for saving the score in specific column according to user input quiz
    match table:
        case "Gk":
            user.gk=correct
            user.save()
        case "Computer":
            user.computer=correct
            user.save()
        case "Animal":
            user.animals=correct
            user.save()
        case "Sport":
            user.sports=correct
            user.save()
        case "Science":
            user.science=correct
            user.save()
        case _:
            return "no column found"
        
    
# code for showing result of the quiz
def result(request):
    if request.method=="POST":
        selected_options=[]   # list for storing options selected by the user
        correct=0

        for i in range(0,20):   # for getting all the answers selected by the user
            op=request.POST.get(f"option{i}")
            if op==correct_answers[i]:
                correct=correct+1
            else:
                pass

            selected_options.append(op)
        
        user_name=request.session.get("user_name")
        table=request.session.get("table")
        
        storing_scores(user_name, table, correct)   # storing score by calling above function

        content={
            "result":f"You have given {correct} correct answers out of 20 questions",
        }
        return render(request, "result.html", content)
    return render(request, "result.html")
