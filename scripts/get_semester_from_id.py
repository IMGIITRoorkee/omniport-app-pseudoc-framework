
mba_map = {
    '310': 1,
    '320': 2,
    '331': 3,
    '341': 4,
    '350': 5,
    '360': 6,
    '371': 7,
    '381': 8
}
mba_sem_id = [int(id) for id in mba_map.keys()]

def get_semester_from_id(semester_id):
    semester_id = int(semester_id)
    if semester_id in mba_sem_id:
        return mba_map[str(semester_id)]
    else:
        semester_id = str(semester_id)
        return (int(semester_id[1])-1)*2+int(semester_id[2])+1