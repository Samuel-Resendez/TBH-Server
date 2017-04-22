from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from TBHServer.models import Entry 
from TBHServer.serializers import EntrySerializer

# Create your views here.

@csrf_exempt
def EntryList(request):

    if request.method == "GET":

        entries = Entry.objects.all()
        serializer = EntrySerializer(entries,many=True)
        return JsonResponse(serializer.data, safe=False)


    elif request.method == "POST":

        data = JsonParser().parse(request)
        serializer = EntrySerializer(data=data)

        if serializer.is_valid():

            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors,status=400)


def EntryDetail(request,pk):
    try:
        entry = Entry.objects.get(pk=pk)
    except:
        return HttpResponse(status=404)
    
    if request.method == "GET":
        serializer = EntrySerializer(entry)
        return JsonResponse(serializer.data)

    elif request.method == "PUT":
        data = JsonParser().parse(request)
        serializer = EntrySerializer(entry, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == "DELETE":
        entry.delete()
        return HttpResponse(status=204)