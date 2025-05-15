from core.base_auth.managers.get_user import get_user


def update_email_addr(data:dict):
    email_updated = data.get('email_address', None)

    if email_updated is '' or None:
        return "Enter a valid email address", 400

    username = data.get('username', None)

    c = get_user(username).person.contact_information.get()

    c.email_address = email_updated
    c.save()

    return "Successfully updated email address", 200