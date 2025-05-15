
from core.base_auth.managers.get_user import get_user



def update_webmail_addr(data:dict):
    webmail_updated = data.get('email_address', None)

    if webmail_updated is '' or None:
        return "Enter a valid institute email address", 400

    username = data.get('username', None)

    c = get_user(username).person.contact_information.get()

    c.institute_webmail_address = webmail_updated
    c.save()

    return "Institute Email updated successfully", 200
