import datetime
from registration.models.student import NewStudent

from core.kernel.models import *


def create_new_student(data, person_object):
    """
    Function to create student for a person
    :param data: data from ACAD API
    :param person_object: the person whose student role to be defined
    :return: student instance created
    """
    sem_id = str(data['SemesterID'])
    try:
        student = NewStudent(
            start_date=datetime.datetime.now(),
            person=person_object,
            enrolment_number=int(data['EnrollmentNo']),
            branch=Branch.objects.get(code=data['ProgramID']),
            current_year=int(sem_id[1]),
            current_semester=(int(sem_id[1]) - 1) * 2 + int(
                sem_id[2]) + 1
        )
    except:
        return None
    try:
        father = person_object.parents.create()
        father.contact_information.create()
        father.save()
        mother = person_object.parents.create()
        mother.contact_information.create()
        mother.save()
        person_object.save()
    except:
        pass
    student.save()

    return student

