import csv
from django.core.management.base import BaseCommand
from django.conf import settings
from entities.models import Entity

class Command(BaseCommand):
    help = 'Load entities from CSV into the database'

    def handle(self, *args, **kwargs):
        Entity.objects.all().delete()  # clear before reload
        with open(settings.BASE_DIR_DATA, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            count = 0
            for row in reader:
                Entity.objects.create(
                    id=row['id'],
                    name=row['name'],
                    country=row['country'],
                    entity_type=row['entity_type'],
                    date_added=row['date_added'],
                    program=row['program'],
                    notes=row['notes'],
                )
                count += 1
        self.stdout.write(self.style.SUCCESS(f'Loaded {count} entities.'))