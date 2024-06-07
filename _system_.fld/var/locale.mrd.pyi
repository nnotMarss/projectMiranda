# import sys, os
# name = os.path.basename(__file__)
# args = []
# sys.path.append(os.path.join(os.getcwd(), "_system_.fld", "lib", ""))
# from miranda_logger import log  # noqa
# import miranda_language as lang  # noqa
# import miranda_folder as folder  # noqa
# if len(sys.argv) > 1:
#     args = sys.argv[1].split()
# existing_lang = open(os.path.join(folder.root(), "_system_.fld", "libdata", "miranda", "LANGUAGE.var"), 'r+')
#
# if existing_lang.read() == "":
#     existing_lang.write("EN")
# print(lang.lang("EN", "language"))
# for locale in lang.lang("all", "all"):
#     print("\n:: %s" % lang.lang(existing_lang.read(), "nothing_done"))
# try:
#     user_lang = input(":]")
#     if user_lang.split() == "" or user_lang.split() is None:
#         print("")
#
# except KeyboardInterrupt:
#     print("\n:: %s" % lang.lang(existing_lang.read(), "nothing_done"))
print(":: Function disabled.")