from django.http import HttpResponse

def homePage(request):
    return HttpResponse('Hello')

def getEggs(request):
    return HttpResponse('Here are some eggs')

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

