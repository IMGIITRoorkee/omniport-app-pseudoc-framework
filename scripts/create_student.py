import datetime
from core.kernel.models import *
from scripts.get_semester_from_id import get_semester_from_id

def create_student(data, person_object):
    """
    Function to create student for a person
    :param data: data from ACAD API
    :param person_object: the person whose student role to be defined
    :return: student instance created
    """
    sem_id = str(data['SemesterID'])

    try:
        student = Student.objects.get(person=person_object)
    except:
        student = Student(
            start_date=datetime.datetime.now(),
            person=person_object,
            enrolment_number=int(data['EnrollmentNo']),
            branch=Branch.objects.get(code=data['ProgramID']),
            current_semester=get_semester_from_id(sem_id)
        )
        student.save()

        try:
            local_guardian = person_object.local_guardians.create()
            local_guardian.contact_information.create()
            father = Person.objects.create(
                full_name=data['Fathersname'].title()
            )
            mother = Person.objects.create(
                full_name=data['MotherName'].title(),
            )
            person_object.parents.add(father)
            person_object.parents.add(mother)
            person_object.save()
        except:
            pass

    return student