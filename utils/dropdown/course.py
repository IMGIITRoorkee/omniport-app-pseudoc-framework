import swapper

Course = swapper.load_model('kernel', 'Course')


def get_courses():
    all_courses= Course.objects.all()
    course_list = [
        {'displayName': course.name, 'value': course.code}
        for course in all_courses
    ]
    return course_list
