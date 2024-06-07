import os
import sys
import json


def parent(directory=os.getcwd(), levels=1):
    parent_dir = os.path.abspath(os.path.join(directory, *([os.pardir] * levels)))
    return parent_dir


sys.path.append(parent())
import miranda_folder as folder  # noqa
tmp_file = open(os.path.join(folder.root(), "_system_.fld", "libdata", "miranda", "LANG.var"), 'r')
strings = json.load(tmp_file)


def lang(locale: str, string: str):
    string = string.lower()+".str"
    locale = locale.upper()
    try:
        if locale == "ALL" and string == "all.str":
            return strings
        else:
            return strings[locale][string]
    except KeyError:
        # log("ERROR", "ENTRY '%s' NOT FOUND IN '%s'" % (string, locale))
        sys.exit(":: Entry '%s' missing in locale '%s'!" % (string, locale))


def select_lang(locale: str):
    try:
        locale = locale.upper()
    except AttributeError:
        pass
    if locale in strings:
        with open(os.path.join(folder.root(), "_system_.fld", "libdata", "miranda", "LANGUAGE.var"), "r+") as f:
            f.write(locale)
        # log("INFO", "LOCALE %s SELECTED" % locale)
        return strings[locale]["locale.str"]
    else:
        return "<<NoLocale%s>>" % locale
    pass


def current_lang():
    return open(os.path.join(folder.root(), "_system_.fld", "libdata", "miranda", "LANGUAGE.var")).read()
