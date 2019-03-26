from django.http import HttpResponse #for direct display without html page
from django.shortcuts import render #to render .html in return 
import operator 

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def submit(request):
    fulltext = request.GET['fulltext'] #get the text inputed by user
    #count total number of words
    wordlist = fulltext.split()
    worddictionary = {}
    for word in wordlist:
        worddictionary[word] = worddictionary.get(word, 0) + 1
    wordsplited = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse = True)
    return render(request, 'submit.html', 
                  {'fulltext':fulltext, 
                   'counted':len(wordlist),
                   'usethis':wordsplited})
