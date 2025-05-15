from scripts.create_user import create_user
from scripts.create_faculty import create_faculty
from scripts.populate_details import populate_details
from scripts.make_request import make_request
def create_faculty_pseudoc_framework(data:dict):
    employee_id = data.get('employee_id', None)

    if employee_id is None:
        return "Enter a valid employee id" , 400

    data_acad = make_request(employee_id, True)

    if data_acad is None:
        return "Data on ACAD profile doesn't exist for this user", 400

    user, person = create_user(employee_id, data_acad)

    try:
        if 'Contract' in data_acad['Designation']:
            data_acad['Designation'] = 'Assistant Professor (contract)'
        elif 'Assistant Professor' in data_acad['Designation']:
            data_acad['Designation'] = 'Assistant Professor'
        elif 'Visiting Faculty' in data_acad['Designation']:
            data_acad['Designation'] = 'Visiting Professor'
        faculty = create_faculty(data_acad, person)
    except:
        return "Error creating faculty", 417

    populate_details(person, data_acad)

    return "Successfully created Faculty", 200
