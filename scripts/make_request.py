import requests
from pseudoc.secrets import ACAD_URL_FACULTY, ACAD_URL_STUDENT, HEADER, NEW_ACAD_URL_STUDENT, NEW_ACAD_URL_FACULTY
def make_request(username, is_faculty=False):
    """
    :param username: username for whom data to be fetched
    :param is_faculty: True if user is a faculty
    :return: dat on success, None otherwise
    """
    try:
        r = requests.get(
            url=f'{NEW_ACAD_URL_STUDENT}{username}' if not is_faculty
                else f'{NEW_ACAD_URL_FACULTY}{username}',
            headers=HEADER,
        )
        data = r.json()
        if isinstance(data, list):
            data = data[0] if len(data)==1 else None
        if not (data or is_faculty):
            r = requests.get(
                url=f'{ACAD_URL_STUDENT}{username}' if not is_faculty
                    else f'{ACAD_URL_FACULTY}{username}',
                headers=HEADER,
            )
            data = r.json()
        return data
    except requests.ConnectionError:
        return None