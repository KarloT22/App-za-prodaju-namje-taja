from main.models import *
from rest_framework import serializers


class KorisnikSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Korisnik
        fields = ['ime', 'prezime', 'mjesto', 'dob', 'vip']

class OglasSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Oglas
        fields = ['prodavatelj', 'predmet', 'mjesto', 'cijena', 'razmjena']
    