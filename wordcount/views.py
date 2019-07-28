from django.http import HttpResponse
from django.shortcuts import render
import operator


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html', {'about':"CoderDjango"})

def count(request):
    what = request.GET['whatever']
    # print(what)
    res = what.split()
    wordcount = {}
    for word in res:
        if word in wordcount:
            wordcount[word] += 1
        else:
            wordcount[word] = 1

    sortedcount = sorted(wordcount.items(), key=operator.itemgetter(1), reverse=False)
    return render(request, 'count.html', {
        'what': what,
        'lent': len(res),
        'sortedcount': sortedcount
    })
