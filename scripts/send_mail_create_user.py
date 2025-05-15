
from services.categories.models import Category
from omniport.settings.configuration.base import CONFIGURATION
from formula_one.utils.verification_token import send_token

from core.kernel.models import *

from services.categories.models import Category
from omniport.settings.configuration.base import CONFIGURATION
from formula_one.utils.verification_token import send_token



def send_mail_create_user(username, user_id, person_id):
    """
    Function to send success mail on user creation
    :param user_id: user id to send the mail to
    :param person_id: person id to send the mail to
    :return: True on success, False otherwise
    """
    site_name = CONFIGURATION.site.nomenclature.verbose_name
    site_url = CONFIGURATION.allowances.hosts[0]

    token_type = 'RECOVERY_TOKEN'
    url = f'https://channeli.in/auth/reset_password/?token={token_type}'
    subject = f'{site_name} account creation'
    body = f'''
            Your Channeli account has been created.
            To reset your {site_name} account password, please visit url'
            '''
    category, _ = Category.objects.get_or_create(name="Auth", slug="auth")
    person_name = Person.objects.get(id=person_id).full_name
    new_account_body = f"""Hi!
    <br><br>
    <b>Please ignore this mail if you're already using channeli</b>
    <br><br>
    Welcome to {site_name}! Pay a visit by logging in at https://channeli.in/ with username as <b>{username}</b> and the account password. To set your account password, please visit the following link.
    <br><br>
    url
    <br><br>
    If the link doesn't work with the username as provided in the mail above, please refer resetting your password from the link: https://iitr.ac.in/channeli/assets/guide.pdf  If the link is expired, generate a new link by clicking on the reset password button on the login screen. Please feel free to contact IMG or Website-Support if you face any issue during password reset, login, or any other functionality.
    <br><br>
    Regards,
    <br>
    Information Management Group"""

    new_student_account_body = f"""Hello {person_name}.
    <br><br>
    <b>Information Management Group welcomes you to IIT Roorkee! </b>
    <br><br>
    Let us introduce you to {site_name}! Your one stop portal for everything related to R-Land. Pay a visit by logging in at https://channeli.in/ with username as <b>{username}</b> and the account password. To set your account password, please visit the following link.
    <br><br>
    url
    <br><br>
    Please refer resetting your password from the link: https://iitr.ac.in/channeli/assets/guide.pdf if the link doesn't work with the username as provided in the mail above. If the link is expired, generate a new link by clicking on the reset password button on the login screen. Please feel free to contact IMG if you face any issue during password reset, login, or any other functionality.
    <br><br>
    Regards,
    <br>
    Information Management Group"""
 

    try:
        send_token(
            user_id=user_id,
            person_id=person_id,
            token_type=token_type,
            email_body=new_student_account_body,
            email_subject=subject,
            url=url,
            category=category
        )
        return True
    except:
        return False

