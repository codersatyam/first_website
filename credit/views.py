# i have created this -- satyam
from django.http import HttpResponse
from django.shortcuts import render
def home(request):

    return render(request,"home.html")
def analysed_text(request):
    djtext = request.GET.get("text", "default")
    removepunc = request.GET.get("remove punctuations", "off")
    upper = request.GET.get("uppercase", "off")
    space= request.GET.get("space remover", "off")
    extra_line = request.GET.get("remove extra line", "off")
    character= request.GET.get("character count", "off")
    punctuations = ",./?(){}%$#@!&*^%"
    analysed = " "
    if removepunc == "on":
        for char in djtext:
            if char in djtext:
                if char not in punctuations:
                     analysed = analysed + char
        params = {"purpose": "remove punctuation", "analyzed_text": analysed}
        return render(request, "analyse.html", params)
    elif upper =="on":
        analysed=djtext.upper()
        params = {"purpose": "capitalise", "analyzed_text": analysed}
        return render(request,"analyse.html", params)
    elif character == "on":
        analysed = len(djtext)
        params = {"purpose": "total character", "analyzed_text": analysed}
        return render(request, "analyse.html", params)
    elif space == "on":
        for char in djtext:
            if char in djtext:
                if " " != char:
                     analysed = analysed + char

        params = {"purpose": "Space removed", "analyzed_text": analysed}
        return render(request, "analyse.html", params)
    elif extra_line == "on":
        for char in djtext:
            if char in djtext:
                if "/n" not in djtext:
                     analysed = analysed + char
        params = {"purpose": "capitalise", "analyzed_text": analysed}
        return render(request, "analyse.html", params)
    else:
        return HttpResponse("<h1>error</h1>")
def about(request):
    return render(request,"about.html")
def contact(request):
    return render(request,"contact.html")






