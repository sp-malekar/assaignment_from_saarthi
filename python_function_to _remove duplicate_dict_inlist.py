def remove_duplicate_dic(List_dic):
    p = {value['id']:value for value in List_dic}.values()
    return p 