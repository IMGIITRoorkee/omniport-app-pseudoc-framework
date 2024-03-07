from categories.models import Category


def get_categories():
    all_categories = Category.objects.all()
    category_list = [
        {'displayName': category.slug, 'value': category.id}
        for category in all_categories
    ]
    return category_list
