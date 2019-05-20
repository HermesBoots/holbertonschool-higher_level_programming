#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    index = 0
    ret = []
    while index < list_length:
        quotient = 0
        try:
            quotient = my_list_1[index] / my_list_2[index]
        except IndexError:
            print('out of range')
        except TypeError:
            print('wrong type')
        except ZeroDivisionError:
            print('division by 0')
        finally:
            ret.append(quotient)
            index += 1
    return ret
