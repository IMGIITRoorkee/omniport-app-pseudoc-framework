from no_dues.models import Authority


def get_no_dues_authorities():
    all_authorities = Authority.objects.all()
    authority_list = [
        {
            'displayName': f"{authority.full_name}: {authority.slug}",
            'value': authority.id
        }
        for authority in all_authorities
    ]
    return authority_list
