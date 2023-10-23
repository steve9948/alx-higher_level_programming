#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            if i >= len(my_list_1) or i >= len(my_list_2):
                print("out of range")
                result.append(0)
            else:
                try:
                    val1 = my_list_1[i]
                    val2 = my_list_2[i]
                    if not isinstance(val1, (int, float)) or not isinstance(val2, (int, float)):
                        print("wrong type")
                        result.append(0)
                    elif val2 == 0:
                        print("division by 0")
                        result.append(0)
                    else:
                        result.append(val1 / val2)
                except ZeroDivisionError:
                    print("division by 0")
                    result.append(0)
        except (TypeError, IndexError):
            pass
    return result
