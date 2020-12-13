import swapper

Centre = swapper.load_model('kernel', 'Centre')


def get_centres():
    all_centres = Centre.objects.all()
    centre_list = [
        {'displayName': centre.name, 'value': centre.code}
        for centre in all_centres
    ]
    return centre_list
