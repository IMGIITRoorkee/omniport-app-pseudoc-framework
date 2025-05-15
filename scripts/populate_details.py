import datetime

from django_countries.data import COUNTRIES


from core.kernel.models import *
from formula_one.models import *

from core.base_auth.models import User
from shell.constants import residences
from scripts.populate_location_info import populate_location_info
from pseudoc.constants import CATEGORIES
from scripts.populate_contact_info import populate_contact_info

def populate_details(person_object, details, update_residential_info = False):
    """
    One function which handles the creation and population of biological info,
    location info, contact info, residential and political info of a person
    :param person_object: person object for whom model instances to be created
    :param details: data from ACAD API
    :return: None
    """
    # --------------------------LocationInfo Creation--------------------------#
    try:
        location_queryset = person_object.location_information.all()
        if len(location_queryset) == 0:
            location_information = LocationInformation.objects.create(
                entity=person_object
            )
        else:
            location_information = location_queryset[0]

        populate_location_info(location_information, details)

    except Exception as e:
        # print(str(e))
        pass
    # -------------------------------------------------------------------------#

    # --------------------------ContactInfo Creation---------------------------#
    try:
        contact_informations = person_object.contact_information.all()
        if len(contact_informations) == 0:
            contact_information = ContactInformation.objects.create(
                entity=person_object
            )
        elif len(contact_informations) == 1:
            contact_information = contact_informations[0]

        populate_contact_info(contact_information, details)

    except Exception as e:
        # print(str(e))
        pass
    # -------------------------------------------------------------------------#

    # --------------------------PoliticalInfo Creation-------------------------#
    try:
        category_code = "oth"  # Default is 'other'
        country_code = "IN"
        religion = (details.get('Religion', "") or '').title()
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

        political_informations = PoliticalInformation.objects.filter(person=person_object)
        if len(political_informations) == 0:
            _ = PoliticalInformation.objects.create(
                person=person_object,
                nationality=country_code,
                religion=religion,
                reservation_category=category_code,
            )
        else:
            political_information = political_informations[0]
            political_information.nationality = country_code
            political_information.religion = religion
            political_information.reservation_category = category_code

            try:
                political_information.save()
            except Exception as e:
                # print(str(e))
                pass

    except Exception as e:
        # print(str(e))
        pass
    # -------------------------------------------------------------------------#

    # ---------------------------BiologicalInfo Creation-----------------------#
    try:

        all_blood_groups = ['O+', 'O-', 'A+', 'A-', 'B+', 'B-', 'AB+', 'AB-']

        # Default = 'O+'
        blood_group = (details.get("BloodGroup", 'O+') or 'O+').upper().\
            strip().replace(
            ' ', '')
        if blood_group not in all_blood_groups:
            blood_group = 'O+'

        # If DoB is not found, mark today's date as Birth Date.
        if details.get("DateofBirth", False):
            dob = datetime.datetime.strptime(details["DateofBirth"], "%d-%m-%Y").date()
        else:
            dob = datetime.datetime.now().date()

        # If gender is not found, mark default sex as non-disclosure
        sex = 'n-dis'
        if details.get('Gender', False):
            sex = details['Gender'].lower()

        # If gender is not found, mark default gender as non-disclosure
        gender = 'n-dis'
        if details.get('Gender', False):
            if details['Gender'].lower().startswith('f'):
                gender = 'woman'
            elif details['Gender'].lower().startswith('m'):
                gender = 'man'

        # If gender is not found, mark default pronoun as 'They/them/their'
        pronoun = 't'
        if details.get('Gender', False):
            if details['Gender'].lower().startswith('f'):
                pronoun = 's'
            elif details['Gender'].lower().startswith('m'):
                pronoun = 'h'

        biological_informations = BiologicalInformation.objects.filter(person=person_object)
        if len(biological_informations) == 0:
            _ = BiologicalInformation.objects.create(
                person=person_object,
                date_of_birth=dob,
                blood_group=blood_group,
                sex=sex,
                gender=gender,
                pronoun=pronoun,
                impairment='n'
            )
        else:
            biological_information = biological_informations[0]
            biological_information.date_of_birth=dob
            biological_information.blood_group=blood_group
            biological_information.sex=sex
            biological_information.gender=gender
            biological_information.pronoun=pronoun
            biological_information.impairment='n'

            try:
                biological_information.save()
            except Exception as e:
                # print(str(e))
                pass

    except Exception as e:
        # print(str(e))
        pass
    # -------------------------------------------------------------------------#

    # ---------------------------FinancialInfo Creation------------------------#
    try:
        _ = FinancialInformation.objects.create(
            person=person_object,
        )
    except Exception as e:
        # print(str(e))
        pass
    # -------------------------------------------------------------------------#

    # ---------------------------ResidentialInfo Creation----------------------#
    try:
        if update_residential_info:
            # default bhawan as 'not a resident'
            bhawan_code = "nor"
            if details.get('Bhawan', False):
                for rr in residences.RESIDENCES:
                    if rr[1].lower() == details['Bhawan'].lower():
                        bhawan_code = rr[0]
                        break

            residential_informations = ResidentialInformation.objects.filter(person=person_object)
            if bhawan_code == "nor" and len(residential_informations) == 0:
                _ = ResidentialInformation.objects.create(
                    person=person_object,
                    residence=Residence.objects.get_or_create(code=bhawan_code)[0],
                    room_number="NIL"
                )
            else:
                _ = ResidentialInformation.objects.create(
                    person=person_object,
                    residence=Residence.objects.get_or_create(code=bhawan_code)[0],
                    room_number=details.get('RoomNo', "NIL")
                )
    except Exception as e:
        # print(str(e))
        pass
    # -------------------------------------------------------------------------#