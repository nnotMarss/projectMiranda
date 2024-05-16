from sys import path
import os
if os.path.exists(os.path.join(".\\", "_system_.fld", "lib")) is False:
    raise IOError("[[SYSTEM FOLDER NOT FOUND!]]")
path.append(os.path.join(".\\", "_system_.fld", "lib"))


class mrd:
    from miranda_logger import log, clear  # noqa: F401
    import miranda_folder as folder  # noqa: F401
    import miranda_function as function


def cons():
    try:
        usr_inp = input("~]")
        func, args = "", []
        try:
            func, *args = usr_inp.lower().split()
        except ValueError:
            pass
        mrd.function.run_func(func.lower()+".pyi", args)

        pass
    except KeyboardInterrupt:
        mrd.log("WARN", "EXIT CODE: KEYBOARD INTERRUPTED")
        exit()


def boot():
    mrd.function.run_func("update_var.pyi", [])
    mrd.log("INFO", "SYSTEM OPERATIONAL")


if __name__ == "__main__":
    boot()
    while True:
        cons()
