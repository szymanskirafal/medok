# from django.contrib import admin

"""
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model

from medok.users.forms import UserChangeForm, UserCreationForm

User = get_user_model()


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):

    form = UserChangeForm
    add_form = UserCreationForm
    fieldsets = (
        (
            "User",
            {
                "fields": (
                    "name",
                    "pesel",
                    "nurse",
                    "doctor",
                    "psychologist",
                    "physiotherapist",
                    "occupational_therapist",
                    "superuser",
                )
            },
        ),
    )
    search_fields = ["name"]
    """
