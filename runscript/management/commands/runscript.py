import os
import sys

from django.core.management import call_command
from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    args = "<path>"
    help = "My help text"

    def handle(self, *args, **options):

        print("Outputs?")
