import os
import sys

from django.core.management import call_command
from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    args = "<path>"
    help = ("Runs a Python script from the command-line, "
            "while providing the Django environment.")

    def handle(self, *args, **options):

        sys.path.append(os.getcwd())

        path = args[0]
        execfile(path)        
