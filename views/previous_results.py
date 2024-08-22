from django.shortcuts import render
from home.models import UserScore

# function for changing value of non-submitted quizes from "None to Quiz not submitted " 
def none_change(lst,):
    for i in lst:
        if i==None:
            index=lst.index(i)
            lst[index]="Quiz not submitted"
        else:
            pass
    return lst


# code for displaying previous results of user according to the quizes submitted by him
def previous(request):
    numbers=list(range(0,5))
    columns=["Gk", "Computer", "Animals", "Sports", "Science"]
    if request.method=="POST":
        user_name=request.session.get("user_name")
        data=UserScore.objects.filter(usern=user_name).values_list("gk", "computer", "animals", "sports", "science")
        data1_tuple=list(data)
        for i in data1_tuple:
            scores= (list(i))
        
        none_change(scores)

    content={
        "numbers":numbers,
        "columns":columns,
        "scores":scores
    }
    return render(request, "previous_score.html", content)
        
