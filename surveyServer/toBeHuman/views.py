from toBeHuman.serializers import EntrySerializer
from toBeHuman.models import Entry
from rest_framework import generics

# Create your views here.
class EntryList(generics.ListCreateAPIView):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer


class EntryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
