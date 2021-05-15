import swapper

Branch = swapper.load_model('kernel', 'Branch')


def get_branches():
    all_branches = Branch.objects.all()
    branch_list = [
        {'displayName': branch.name, 'value': branch.code}
        for branch in all_branches
    ]
    return branch_list
