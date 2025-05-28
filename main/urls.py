from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("signup/", views.signup, name="signup"),
    path("polls/", views.polls_list, name="polls"),
    path("polls/<int:question_id>/", views.poll_detail, name="poll_detail"),
    path('bizkimiz/', views.biz_kimiz, name='biz_kimiz'),
    path('yarislarimiz/', views.yarislarimiz, name='yarislarimiz'),
    path('yelkenhakkinda/', views.yelken_hakkinda, name='yelken_hakkinda'),
    path('basarilarimiz/', views.basarilarimiz, name='basarilarimiz'),
    path('about/', views.about, name='about'),
    path('races/', views.yarislarimiz, name='yarislarimiz'),
    path('theory/', views.theory, name='theory'),
    path('practice/', views.practice, name='practice'),
]

