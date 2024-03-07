from noticeboard.models import Banner


def get_noticeboard_banners():
    all_banners = Banner.objects.all()
    banner_list = [
        {'displayName': f'{banner.category_node.parent.name} | {banner.name}', 'value': banner.id}
        for banner in all_banners
    ]
    return banner_list
