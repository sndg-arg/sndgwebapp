from django.http import HttpResponse


def main_page(request):
    return HttpResponse("Hello, world. You're at the polls index.")