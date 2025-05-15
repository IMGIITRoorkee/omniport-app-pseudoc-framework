import datetime
from shell.models import *
from pseudoc.constants import CATEGORIES, DESIGNATION_DICT, DEPTS, CENTRES
def create_faculty(data, person_object):
    """
    Function to create faculty for a person
    :param data: data from ACAD API
    :param person_object: the person whose faculty role to define
    :return: faculty instance created
    """
    
    try:
        content_object = Department.objects.get(
                code=DEPTS[data['DepartmentAlphaCode'].lower()]
            )
    except KeyError:
        content_object = Centre.objects.get(
                 code=CENTRES[data['DepartmentAlphaCode'].lower()] 
            )

    faculty = FacultyMember.objects.get_or_create(
        employee_id=int(data['EmployeeNo']),
        defaults={
            'content_object': content_object,
            'start_date': datetime.datetime.now(),
            'person': person_object,
            'designation': DESIGNATION_DICT.get(
                data['Designation'].lower().strip()
            ),
        }
    )

    return faculty
