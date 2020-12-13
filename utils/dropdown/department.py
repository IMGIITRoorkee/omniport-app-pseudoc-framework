import swapper

Department = swapper.load_model('kernel', 'Department')


def get_departments():
    all_departments = Department.objects.all()
    department_list = [
        {'displayName': department.name, 'value': department.code}
        for department in all_departments
    ]
    return department_list
