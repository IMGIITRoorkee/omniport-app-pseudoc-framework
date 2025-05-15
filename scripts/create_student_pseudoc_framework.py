from scripts.create_user import create_user
from scripts.create_student import create_student
from scripts.populate_details import populate_details
from scripts.make_request import make_request

def create_student_pseudoc_framework(data:dict):
    enrolment_number = data.get('enrolment_number', None)

    if enrolment_number is None:
        return "Enter a valid enrolment number" , 400

    data_acad = make_request(enrolment_number, False)
    
    if data_acad is None:
        return "Data on ACAD profile doesn't exist for this user", 400


    user, person = create_user(enrolment_number, data_acad)

    try:
        student = create_student(data_acad, person)
    except:
        return "Error creating student", 417

    populate_details(person, data_acad)
    contact = person.contact_information.get()

    if contact.institute_webmail_address is None:
        contact.institute_webmail_address = data_acad['IITREmailID']
        print(enrolment_number)
        contact.save()

    print(f'{person} ::: {person.contact_information.get()}')

    return "Successfully created Student", 200

