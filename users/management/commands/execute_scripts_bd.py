from typing import Any
from django.core.management.base import BaseCommand
from users.scripts.bd.create_default_role import execute_create_groups

class Command(BaseCommand):
    help = "Ejecuta scripts para poblar la bd"
    def handle(self, *args: Any, **options: Any) -> str | None:
        # Add list functions for execute script in bd
        execute_create_groups()
