#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        div = 0
        div = a / b
    except ZeroDivisionError:
        div = None
    finally:
        print("Inside result: {}".format(div))
        return div
