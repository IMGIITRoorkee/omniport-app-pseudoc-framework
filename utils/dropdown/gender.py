from kernel.constants import biological_information


def get_gender():
    genders = [
        {'displayName': x[1], 'value': x[0]}
        for x in biological_information.GENDERS
    ]
    return genders
