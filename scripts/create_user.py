
from django.db import IntegrityError

from core.kernel.models import *
from formula_one.models import *
from shell.models import *
from core.base_auth.models import User

def create_user(username, acad_data):
    """
    Function to create a user and person instancec for omniport
    :param username: Username of the user to be created
    :param acad_data: Data from the acad API, which we use to create user
    :return: user and person instance created
    """
    user, _ = User.objects.get_or_create(
        username=username,
    )
    try:
        person, person_created = Person.objects.get_or_create(
            user=user,
            full_name=acad_data['Name'].title(),
        )
    except IntegrityError:
        person = Person.objects.get(
            user=user
        )
        person.full_name = acad_data['Name'].title()
        person.save()

    return user, person
