import datetime

from django_countries.data import COUNTRIES
from services.categories.models import Category
from omniport.settings.configuration.base import CONFIGURATION
from django.utils.crypto import get_random_string
from scripts.make_request import make_request
from shell.registration.scripts.auth.create_staff_old import *
from services.emails.actions import email_push
from pseudoc.constants import CATEGORIES
from registration.models.biological_information import NewBiologicalInformation
from registration.models.political_information import NewPoliticalInformation
from registration.models.new_person import NewPerson
from scripts.create_new_student import create_new_student
from scripts.populate_contact_info import populate_contact_info
from scripts.populate_location_info import populate_location_info
def send_mail_registration(username, secret_key, person_object, email_address):
    """
    Function to send success mail on user updation
    :param person_object: person to send the mail to
    :return: True on success, False otherwise
    """
    site_name = CONFIGURATION.site.nomenclature.verbose_name
    category, _ = Category.objects.get_or_create(name="Auth", slug="auth")
    email_subject = f'Welcome to {site_name}!'
    email_body = f"""
            Greeting {person_object.full_name}!
            <br/><br/>
            Now that you are officially a part of the R-Land family we welcome you to the official
            intranet(and for unforseen times like COVID-19, internet) portal of IIT Roorkee, Channel i.
            <br/><br/>
            Channel i is the name you'll be hearing quite a lot during your stay at R-Land, so let's get
            started! Please visit this URL https://internet.channeli.in/registration/register_student and use your enrolment number with the following registration key to register yourself:
            <br/><br/>
            Registration Key: <b>{secret_key}</b>
            <br><br/>
            Why Channeli? Read here: https://medium.com/img-iit-roorkee/channeli-with-love-11cc10dfb6e1
            <br><br>
            Please feel free to contact IMG if you face any further issues.
            <br><br>
            Regards,
            <br>
            Information Management Group
            """

    try:
        email_push(subject_text=email_subject, body_text=email_body,
                   category=category, has_custom_user_target=True,
                   email_ids=[email_address],
                   target_app_name=None,
                   target_app_url=None)
        return True
    except:
        return False


def create_new_omniport_student(enrolment_number, err_list):

    details = make_request(enrolment_number, False)

    if details is None:
        err_list.append(enrolment_number)
        return False
    secret = get_random_string(8)
    new_person = NewPerson.objects.create(full_name=details['Name'].title(), secret_code=secret)

    contact_info = new_person.contact_information.create()
    location_info = new_person.location_information.create()

    local_guardian = new_person.local_guardians.create()
    local_guardian.contact_information.create()

    if not populate_contact_info(contact_info, details):
        err_list.append(enrolment_number)
        return False

    if not populate_location_info(location_info, details):
        err_list.append(enrolment_number)
        return False

    email_address = details.get(
        'PRIEMAIL',
        details['IITREmailID']
    )
    try:
        category_code = "oth"  # Default is 'other'
        country_code = "IN"
        try:
            category_code = CATEGORIES.get(details.get("Category", "other"),
                                           'oth')
            nationality = details.get('Nationality', '') or \
                          details.get('Pcountry', '') or ''
            for c, v in COUNTRIES.items():
                if v.lower() == nationality.lower():
                    country_code = c
                    break
        except:
            pass

        _ = NewPoliticalInformation.objects.create(
            person=new_person,
            nationality=country_code,
            religion=(details.get('Religion', "") or '').title(),
            reservation_category=category_code,
        )
    except:
        err_list.append(enrolment_number)
        return False

    try:

        all_blood_groups = ['O+', 'O-', 'A+', 'A-', 'B+', 'B-', 'AB+', 'AB-']

        # Default = 'O+'
        blood_group = (details.get("BloodGroup", 'O+') or 'O+').upper().\
            strip().replace(
            ' ', '')
        if blood_group not in all_blood_groups:
            blood_group = 'O+'

        _ = NewBiologicalInformation.objects.create(
            person=new_person,

            # If DoB is not found, mark today's date as Birth Date.
            date_of_birth=datetime.datetime.strptime(
                details["DateofBirth"], "%Y-%m-%dT%H:%M:%S"
            ).date() \
                if details.get("DateofBirth", False) else
            datetime.datetime.now().date(),

            blood_group=blood_group,

            # If gender is not found, mark default sex as male
            sex=details['Gender'].lower() \
                if details.get('Gender', False) else 'male',

            # If gender is not found, mark default gender as man
            gender='woman' \
                if (details.get('Gender', False)
                    and details['Gender'].lower().startswith('f')) \
                else 'man',

            # If gender is not found, mark default pronoun as 'he/his/him'
            pronoun='s' \
                if (details.get('Gender', False)
                    and details['Gender'].lower().startswith('f')) \
                else 'h',

            impairment='n'
        )
    except:
        err_list.append(enrolment_number)
        return False

    if create_new_student(details, new_person) is None:
        err_list.append(enrolment_number)
        return False

    send_mail_registration(enrolment_number, secret, new_person, email_address) 

    return True

