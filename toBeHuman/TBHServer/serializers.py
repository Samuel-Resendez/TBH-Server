from rest_framework import serializers 
from TBHServer.models import Entry


class EntrySerializer(serializers.ModelSerializer):
   


   class Meta:
       model = Entry
       fields = ('id','qOneResponse','qTwoResponse','qThreeResponse','qFourResponse')