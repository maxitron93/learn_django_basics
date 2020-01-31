from django.http import HttpResponse
from django.shortcuts import render # This is how to render the templates
import operator

def homePage(request):
    values = {
        'subTitle': 'Write some text and we\'ll count the words for you!'
        }
    return render(request, 'home.html', values)

def getEggs(request):
    return HttpResponse('Here are some eggs')

def countWords(request):
    text = request.GET['text'] # This is how to get params from a request with a form submission
    textArr = text.split()
    textDict = {}
    
    for word in textArr:
        if word in textDict:
            textDict[word] += 1
        else:
            textDict[word] = 1

    data = {
        'text': text,
        'wordCount': len(textArr),
        'textDict': textDict    
    }

    return render(request, 'countWords.html', data)


def about(request):
    return render(request, 'about.html')


def overview(request):
    return HttpResponse(
        '''
        <ol>
        <li>Client send request to url</li>
        <li>django looks for matching path in urls.py</li>
        <li>If mathing url is found, returns the function defined in the second argument of path()</li>
        <li>The function is defined in another module, and imported in</li>
        </ol>
        '''
    )

