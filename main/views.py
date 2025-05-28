from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from polls.models import Question

def home(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    return render(request, "main/home.html", {"latest_question_list": latest_question_list})

def about(request):
    return render(request, "main/about.html")

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("main:home")
    else:
        form = UserCreationForm()
    return render(request, "main/signup.html", {"form": form})

def polls_list(request):
    questions = Question.objects.order_by("-pub_date")
    return render(request, "main/polls.html", {"questions": questions})

def poll_detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "main/poll_detail.html", {"question": question})

def home(request):
    return render(request, "main/home.html")

from django.shortcuts import render

def home(request):
    return render(request, 'main/home.html')

def biz_kimiz(request):
    return render(request, 'main/bizkimiz.html')

def yarislarimiz(request):
    return render(request, 'main/yarislarimiz.html')

def yelken_hakkinda(request):
    return render(request, 'main/yelkenhakkinda.html')

def basarilarimiz(request):
    return render(request, 'main/basarilarimiz.html')
def about(request):
    return render(request, 'main/about.html')
def yarislarimiz(request):
    return render(request, 'main/yarislarimiz.html')
def theory(request):
    return render(request, 'main/theory.html')
def practice(request):
    return render(request, 'main/practice.html')

