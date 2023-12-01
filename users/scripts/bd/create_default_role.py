from django.contrib.auth.models import Group
from users.enums import Groups


def create_groups(groups: Groups):
    for group in groups:
        _, created = Group.objects.get_or_create(name=group.value)
        if created:
            print(f"Gupo: '{group.value}' creado.")
        else:
            print(f"Grupo: '{group.value}' ya existe, no se creó.")


def execute_create_groups():
    create_groups(Groups)
