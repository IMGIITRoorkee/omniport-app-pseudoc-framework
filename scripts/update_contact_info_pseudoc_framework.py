
from core.kernel.models import *
from formula_one.models import *
from shell.models import *
from scripts.populate_contact_info import populate_contact_info
from scripts.make_request import make_request

from core.base_auth.managers.get_user import get_user



def update_contact_info_pseudoc_framework(data:dict):
    username = data.get('username', None)

    if username is None:
        return "Enter a valid enrolment number/employee id", 400

    data_acad = make_request(username, True)

    if data_acad is None:
        data_acad = make_request(username, False)

    if data_acad is None:
        return "Data on ACAD Profile doesn't exist", 417

    try:
        contact_info = get_user(username).person.contact_information.get()
    except:
        return "Error retrieving contact info", 417
    if populate_contact_info(contact_info, data_acad):
        return "Info updated successfully", 200
    return "Error updating contact info", 417
