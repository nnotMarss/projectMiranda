from sys import path
import os
if os.path.exists(os.path.join(".\\", "_system_.fld", "lib")) is False:
    raise IOError("[[SYSTEM FOLDER NOT FOUND!]]")
path.append(os.path.join(".\\", "_system_.fld", "lib"))


class mrd:
    from miranda_logger import log, clear  # noqa: F401
    import miranda_folder as folder  # noqa: F401
    import miranda_function as function
    from miranda_language import lang  # noqa
    user_lang = open(os.path.join(folder.root(), "_system_.fld", "libdata", "miranda", "LANGUAGE.var"), "r").read()


def cons():
    try:
        usr_inp = input("!\\ @ ID%s]" % open(
            os.path.join(mrd.folder.root(), "_system_.fld", "libdata", "miranda", "ID.var"), 'r').read()
                        )
        func, args = "", []
        try:
            func, *args = usr_inp.split()
        except ValueError:
            pass
        mrd.function.run_func(func.lower()+".mrd.pyi", args)

    except KeyboardInterrupt:
        mrd.log("WARN", "EXIT CODE: KEYBOARD INTERRUPTED")
        exit()


def login_tmp():  # TEMPORARY SOLUTION
    users_temp = {"apex": "root", "m4rs_fox": "mars"}
    username = input("name.str]")
    password = input("password.str]")
    if username in users_temp:
        if password == users_temp[username]:
            return 1
        else:
            print("incorrect.str")
            return 0
    else:
        print("notFound.str")
        return 0


def boot():
    mrd.function.run_func("update_var.mrd.pyi", [])
    mrd.log("INFO", "SYSTEM OPERATIONAL")
    print(":: %s" % mrd.lang(mrd.user_lang, "welcome_new"))


if __name__ == "__main__":
    boot()
    # while True:
    #     if login_tmp() == 1:
    #         break
    while True:
        cons()
