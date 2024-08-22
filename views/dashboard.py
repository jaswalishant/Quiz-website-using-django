from django.shortcuts import render, redirect
from home.models import  Gk, Computer, Animal, Sport, Science
import random

option=[]   # list for options (in form of QuerySet and tuple)
questions_list=[]   # list for questions
options=[]  # list for options (unshuffled and in form of a list, not in tuple)
shuffle=[]  # list for options (shuffled)
correct_answers=[]  # list for correct options 

# function for storing data (questions and options) for quizes according to user input
def data_fetch(table):
    if len(questions_list)<=20:  # for not repeating the list, if length exceeds then desired then clear the lists and insert data again
        option.clear()
        questions_list.clear()
        options.clear()
        shuffle.clear()
        correct_answers.clear()

        # inserting data
        if len(questions_list)==0:
            for i in range(1,21):
                question=table.objects.filter(id=i).values_list('question') # inserting questions accoreding to id
                for Question in question:
                    for Q in Question:
                        questions_list.append(Q)
                data=table.objects.filter(id=i).values_list("correct", "incorrect1", "incorrect2", "incorrect3")    # inserting options accoreding to id
                for values in data:
                    option.append(values)
                correct=table.objects.filter(id=i).values_list("correct")   # inserting correct options accoreding to id
                for values in correct:
                    for value in values:
                        correct_answers.append(value)

            for i in option:    # changing a single tuple with multiple values into a single list
                list1=list(i)
                options.append(list1)

            for i in options:   # shuffling the options
                random.shuffle(i)
                shuffle.append(i)
        return questions_list, shuffle


# code for displaying list of quizes 
def dashboard(request):
    numbers=list(range(0,5))   # creating a list of numbers as range function does not word in django html template
    lst=["Gk", "Computer", "Animal", "Sport", "Science"]   # creating list of quizes available
    name=request.session.get('user_name')
    content={
        "name":name,
        "numbers":numbers,
        "lst":lst
    }
    if name != None:
        if request.method=='POST':
            request.session["table"]=request.POST.get('table_name')
            table=request.session["table"]

            # code for displaying the quiz according to user input
            match table:
                case "Gk":
                    print(table)
                    data_fetch(Gk)
                    return redirect("get_data")
                case "Computer":
                    data_fetch(Computer)
                    return redirect("get_data")
                case "Animal":
                    data_fetch(Animal)
                    return redirect("get_data")
                case "Sport":
                    data_fetch(Sport)
                    return redirect("get_data")
                case "Science":
                    data_fetch(Science)
                    return redirect("get_data")
                case _:
                    return render(request, "dashboard.html", content)
    else:
        return redirect("login_user")
    return render(request, "dashboard.html", content)


# function for returning lists into different .py files
def returning_lists():
    return questions_list, shuffle, correct_answers