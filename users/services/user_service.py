from users.models import User
from django.contrib.auth.models import Group

class UserService:
    @classmethod
    def create_vendedor(cls, cleaned_data):
        vendedor = User.objects.create(
            first_name=cleaned_data["first_name"],
            last_name=cleaned_data["last_name"],
            email=cleaned_data["email"],
            username=cleaned_data["username"],
        ) 
        vendedor.set_password(cleaned_data["password"])
        grupo = Group.objects.get(name="vendedor")
        vendedor.groups.add(grupo)
        vendedor.save()
        return vendedor

