
def create_staff_pseudoc_framework(data:dict):
    errors_uname = create()

    if len(errors_uname) == 0:
        return "Succesfully created all staff", 200
    unames = ''

    for uname in errors_uname:
        unames += f'{uname} '
    return f'Error creating following employees {unames}', 417 

