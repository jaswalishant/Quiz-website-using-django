from django.contrib import admin
from django.urls import path
from home import views
from views.register import register_user
from views.login import login_user, logout_user
from views.dashboard import dashboard
from views.quiz_display import get_data
from views.result_and_storing_score import result
from views.correct_answers import check_answers
from views.previous_results import previous

urlpatterns = [
    path('', register_user, name="register_user"),
    path('login', login_user, name="login_user" ),
    path('dashboard', dashboard, name="dashboard"),
    path('logout', logout_user, name="logout_user"),
    path('quiz', get_data, name="get_data"),
    path('result', result, name="result"),
    path('check_answers', check_answers, name="check_answers"),
    # path('entry', views.entry, name="entry"),
    path('previous_score', previous, name="previous_score"),
    ]
