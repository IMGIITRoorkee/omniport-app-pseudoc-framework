
from django.db import IntegrityError

from core.base_auth.managers.get_user import get_user

def populate_contact_info(contact_information, details):
    """
    Function to populate the contact info of a person based on ACAD API data
    :param contact_information: location information instance
    :param details: data from ACAD API
    :return: True if successful, False otherwise
    """
    try:
        contact_information.primary_phone_number = details.get(
            'Mobileno', None
        )
        contact_information.secondary_phone_number = details.get(
            'ContactNo', None
        )
        if contact_information.secondary_phone_number == '':
            contact_information.secondary_phone_number = None
        contact_information.email_address = details.get('EmailID', None)

        institute_email_id = details['IITREmailID']
        if not contact_information.institute_webmail_address or contact_information.institute_webmail_address != institute_email_id:
            try:
                contact_information.institute_webmail_address = institute_email_id
            except IntegrityError:
                person2 = get_user(institute_email_id).person
                contact2 = person2.contact_information.get()
                contact2.institute_webmail_address = None
                contact2.save()

                contact_information.institute_webmail_address = institute_email_id
            except Exception as e:
                return False

        contact_information.save()
        return True
    except:
        return False

