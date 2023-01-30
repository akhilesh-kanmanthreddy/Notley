from django.shortcuts import render

import openai
import easyocr


def index(request):
    return render(
        request,
        "index.html",
        {
            "title": "Django example",
        },
    )


def topictonotes(request):
    return render(request, "topictonotes.html")


def expandontopic(request):
    return render(request, "expandontopic.html")


def topictoflashcards(request):
    return render(request, "topictoflashcards.html")


def topictopracticetest(request):
    return render(request, "topictopractice.html")


def output(request):
    text = request.GET["text"]
    #import openai
    openai.api_key = "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"
    response = openai.Completion.create(
     model="text-davinci-003",
    prompt="condense this paragraph into bullet point notes, using hashtags to seperate them" + text,
    temperature=0.3,
     max_tokens=1000,
    top_p=1.0,
    frequency_penalty=0,
     presence_penalty=0,
    )
    response1 = response['choices'][0]['text']
    response2 = response1.split("#")
    return render(request, 'output.html', {'response':response2})


def imagetotext(request):
    image = request.GET["fileUpload"]
    reader = easyocr.Reader(['en'])
    results = reader.readtext(image)
    text = ''
    for i in results:
        text += i[1] + ' '
    #import openai
    openai.api_key = "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"
    response = openai.Completion.create(
     model="text-davinci-003",
    prompt="condense this paragraph into bullet point notes, usiing hashtags as bullet points" + text,
    temperature=0.3,
     max_tokens=1000,
    top_p=1.0,
    frequency_penalty=0,
     presence_penalty=0,
    )
    response1 = response['choices'][0]['text']
    response2 = response1.split("#")
    return render(request, 'imagetotext.html',{'response':response2})