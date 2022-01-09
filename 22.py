def list_op(input_list):
    if len(input_list) == 0:
        return
    else:
        print (input_list[0], end= " ")
        list_op (input_list[:0:-1])
list_op([1, 2, 3, 4, 5])