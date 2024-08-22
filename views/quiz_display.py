from django.shortcuts import render
from views.dashboard import returning_lists

# code for displaying quiz to the user
def get_data(request):
    questions_list=returning_lists()[0]   # getting questions from dashboard.py file using function and index for return value
    shuffle=returning_lists()[1]   # getting shuffled options from dashboard.py file using function and index for return value 

    numbers=list(range(0,len(questions_list)))
    content={
        "question":questions_list,
        "option":shuffle,
        "numbers":numbers
    }
    return render(request, "quiz.html", content)
