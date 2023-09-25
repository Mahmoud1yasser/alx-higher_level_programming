#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    div = 0
    new_list = []
    for items in range list_lenght:
        try:
            div = my_list_1[items] / my_list_2[items]
        except TypeError:
            div = 0
            print("wrong type")
        except IndexError:
            div = 0
            print("out of range")
        except ZeroDivisionError:
            div = 0
            print("division by 0")
        finally:
            new_list = new_list + [div]
    return new_list

