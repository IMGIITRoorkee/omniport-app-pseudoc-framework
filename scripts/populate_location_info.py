

from django_countries.data import COUNTRIES

def populate_location_info(location_information, details):
    """
    Function to populate the location info of a person based on ACAD API data
    :param location_information: location information instance
    :param details: data from ACAD API
    :return: True if successful, False otherwise
    """
    try:
        country_code = "IN"
        nationality = details.get('Nationality', '') or \
                      details.get('Pcountry', '') or ''
        for c, v in COUNTRIES.items():
            if v.lower() == nationality.lower():
                country_code = c
                break

        location_information.address = details.get(
            'PermanentAddress', ''
        ) or ''
        location_information.state = details.get('State', '') or ''
        location_information.city = details.get('City', '') or ''
        location_information.country = country_code

        location_information.save()

        return True
    except:
        return False
