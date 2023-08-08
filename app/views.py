from django.shortcuts import render


def create_links(request):
    context = {}
    return render(request, 'index.html', context)

def index_page(request):
    context = {}
    return render(request, 'index.html', context)
