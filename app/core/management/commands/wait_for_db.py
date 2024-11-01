"""
Django command to wait for database to be available
"""

from django.core.management.base import BaseCommand

from django.db.utils import OperationalError
from django.db import connections


class Command(BaseCommand):
    """Django command to pause execution until database is available"""
    def handle(self, *args, **options):
        pass
