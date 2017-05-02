from rest_framework import serializers
from toBeHuman.models import Entry


class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = ('id','created', 'q1','q2','q3','q4')
