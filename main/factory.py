import factory
from factory.django import DjangoModelFactory
from main.models import *

## Defining a factory
class KorisnikFactory(DjangoModelFactory):
    class Meta:
        model = Korisnik

    ime = factory.Faker("first_name")
    prezime = factory.Faker("last_name")
    dob = factory.Faker("random_int", min=18, max=80)
    mjesto = factory.Faker("city")
    vip = factory.Faker("boolean")

class OglasFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Oglas
        
    prodavatelj = factory.SubFactory(KorisnikFactory)  
    predmet = factory.Faker(
        "random_element",
        elements=[
            "Stol",
            "Televizor",
            "Bicikl",
            "Kauč",
            "Mobitel",
            "Fiksni telefon",
            "Laptop",
            "Frižider",
            "Ormar",
            "Stolac",
        ],
    )
    mjesto = factory.Faker("city")
    cijena = factory.Faker("random_int", min=10, max=10000)
    razmjena = factory.Faker("boolean")
