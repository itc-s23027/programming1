import time


def show_begin_end(func):
    def deco_func(*args, **kwargs):
        print("==start")
        result = func(*args, **kwargs)
        print("== end")
        return result

    return deco_func


def sleep_for_a_while():
    print("Sleeping ..")
    time.sleep(2)
    print("Done Sleeping")


sleep_for_a_while()
