"""
Dango command to wait for the database to be available.
"""
import time
from django.db import OperationalError
from psycopg2 import OperationalError as psycopg2OpError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Dajngo command to wait for database."""
    def handle(self, *args, **options):
        self.stdout.write('Waiting for db...')
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except(psycopg2OpError, OperationalError):
                self.stdout.write('DataBase is unavailable, wait 1 second..')
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS('DataBase is available..'))
