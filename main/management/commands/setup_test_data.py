import random
from django.db import transaction
from django.core.management.base import BaseCommand
from main.models import *
from main.factory import *

NUM_KOR = 100
NUM_OGL = 100

class Command(BaseCommand):
    help = "Generates test data"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting old data...")
        models = [Korisnik, Oglas]
        for m in models:
            m.objects.all().delete()

        self.stdout.write("Creating new data...")

        for _ in range(NUM_KOR):
            korisnik = KorisnikFactory()

        for _ in range(NUM_OGL):
            oglas = OglasFactory()