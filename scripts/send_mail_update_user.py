
from omniport.settings.configuration.base import CONFIGURATION
from services.categories.models import Category
from services.emails.actions import email_push

mba_map = {
    '310': 1,
    '320': 2,
    '331': 3,
    '341': 4,
    '350': 5,
    '360': 6,
    '371': 7,
    '381': 8
}
mba_sem_id = [int(id) for id in mba_map.keys()]

def send_mail_update_user(person_object):
    """
    Function to send success mail on user updation
    :param person_object: person to send the mail to
    :return: True on success, False otherwise
    """
    site_name = CONFIGURATION.site.nomenclature.verbose_name
    category, _ = Category.objects.get_or_create(name="Auth", slug="auth")
    email_subject = f'{site_name} account information updation'
    email_body = f'''
            Hello {person_object.full_name}.
            <br><br>
            Your {site_name} account's information has been updated,
            Please recheck the updated changes by logging into your
            account at https://newchanneli.iitr.ac.in
            <br><br>
            Please feel free to contact IMG if you face any further issues.
            <br><br>
            Regards,
            <br>
            Information Management Group
            '''

    try:
        email_push(subject_text=email_subject, body_text=email_body,
                   category=category, has_custom_user_target=True,
                   persons=[person_object.id],
                   target_app_name=None,
                   target_app_url=None)
        return True
    except:
        return False