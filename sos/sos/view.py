from django.http import HttpResponse


def test_sos (request):
    return HttpResponse('<h1>welcome host</h1>')

def home_sos(request):
    return HttpResponse('welcome to home page')


