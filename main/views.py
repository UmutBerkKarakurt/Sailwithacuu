from django.http import HttpResponse

def index(request):
    return HttpResponse("Merhaba, SailWithAcu ana sayfasına hoş geldiniz")
