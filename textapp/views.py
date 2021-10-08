# meri file hai bc pareshan hogya
from django.http import HttpResponse
from django.shortcuts import render


def index(response):
    return render(response, 'index.html')


def analyze(response):
    djtext = response.GET.get('text', 'default')
    removepunc = response.GET.get('removepunc', 'off')
    uppercase = response.GET.get('capital', 'off')
    newlineremover = response.GET.get('newlineremove', 'off')
    extraspace = response.GET.get('extraspace', 'off')
    charcount = response.GET.get('charcount', 'off')
    if removepunc == "on":
        punctuation = '''!"#$%&'()*+, -./:;<=>\?@[]^_`{|}~'''
        analyzed = ''
        for char in djtext:
            if char not in punctuation:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        return render(response, 'analyze.html', params)
    elif uppercase == "on":
        analyzed = ''
        analyzed = analyzed + djtext.upper()
        params = {'purpose': 'UPPERCASE', 'analyzed_text': analyzed}
        return render(response, 'analyze.html', params)

    elif newlineremover == "on":
        djtext = djtext.replace('\r\n', '').replace('\n', '')
        analyzed = ''
        for char in djtext:
            if not (char == " "):
                analyzed = analyzed + char
                djtext = analyzed
        params = {'purpose': 'new lines removed', 'analyzed_text': analyzed}
        return render(response, 'analyze.html', params)
    elif extraspace == "on":
        analyzed = ''
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char
            params = {'purpose': 'Removed extra spaces', 'analyzed_text': analyzed}
        return render(response, 'analyze.html', params)
    elif charcount == "on":
        analyzed = 0
        for char in djtext:
            if char !=' ':
                analyzed = analyzed+1
                params = {'purpose': 'character count', 'analyzed_text': analyzed}
        return render(response, 'analyze.html', params)




    else:
        return HttpResponse('ERROR!')
