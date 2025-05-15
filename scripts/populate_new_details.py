import datetime

from django_countries.data import COUNTRIES
from pseudoc.constants import CATEGORIES
from registration.models.biological_information import NewBiologicalInformation
from registration.models.political_information import NewPoliticalInformation
def populate_new_details(details, new_person):

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
        pass

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
        pass
