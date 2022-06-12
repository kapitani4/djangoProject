import csv
from csv import DictReader
from django.core.management import BaseCommand

from aviadb.models import Drawing, Compartments

ALREDY_LOADED_ERROR_MESSAGE = """
If you need to reload the child data from the CSV file,
first delete the db.sqlite3 file to destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables"""


class Command(BaseCommand):
    # Show this when the user types help
    help = "Loads data from csv"

    def handle(self, *args, **options):

        filename = 'draw/'+input('Введите название файла: \n')+'.csv'

        # Show this before loading the data into the database
        print("Loading data")

        # Code to load the data into database
        #draw/AN-148.csv

        with open(filename, newline='', encoding='utf-8') as csvfile:
            readFile = csv.DictReader(csvfile)
            for row in readFile:
                draw = Drawing(
                    plan=row['plan'],
                    equipment=row['equipment'],
                    material=row['material'],
                    square = row ['square'],
                    weight = row ['weight'],
                    diamino = row ['diamino'],
                    laser3d = row ['laser3d'],
                    revision = row ['revision'],
                    samplesAreWitnesses = row ['samplesAreWitnesses'],
                    executor = row ['executor'],
                    quantityA4 = row ['quantityA4'],
                    name = row['name'],
                    detail = Compartments.objects.get(id=row['Key_t2'])
                )
                draw.save()
