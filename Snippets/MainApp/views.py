from django.http import Http404
from django.shortcuts import render, redirect
from MainApp.models import Snippet



def index_page(request):
    context = {'pagename': 'PythonBin'}
    return render(request, 'pages/index.html', context)


def add_snippet_page(request):
    context = {'pagename': 'Добавление нового сниппета'}
    return render(request, 'pages/add_snippet.html', context)


def snippets_page(request):
    snippets = Snippet.objects.all()
    print(snippets)
    context = {
        "pagename": "Просмотр сниппетов",
        "snippets": snippets
    }
    # return render(request, 'items_list.html', context
    # context = {'pagename': 'Просмотр сниппетов'}
    return render(request, 'pages/view_snippets.html', context)



def single_snippet_page(request, id):
    try:
        snippet = Snippet.objects.get(id=id)
    except ObjectDoesNotExist:
        raise Http404
    context = {
        'pagename': 'Страница сниппета',
        "snippets": snippet
    }
    return render(request, 'pages/snippet_page.html', context)