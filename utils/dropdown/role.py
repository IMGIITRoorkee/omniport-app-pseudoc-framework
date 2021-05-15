from django.conf import settings


def get_roles():
    roles = settings.ROLES
    role_list = [{'displayName':role, 'value': role} for role in roles]
    return role_list
