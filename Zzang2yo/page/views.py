from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request, 'page/main.html')

def map(request):
    return render(request, 'page/map.html')

