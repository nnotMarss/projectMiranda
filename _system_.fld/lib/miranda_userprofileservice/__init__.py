import os, sys  # noqa
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), *([os.pardir] * 1))))
import miranda_folder as folder  # noqa
import mars_file as file  # noqa

#
# TO DO: SET UP LOGS BITCH WHEN ALL THE STUFF IS READY
#


def get_users_list():
    profiles_list = sorted(
        user for user in os.listdir(
            os.path.join(folder.root(), "_system_.fld", "users", "")
        ) if user.endswith(".mups.mfc")
    )
    return profiles_list


def get_user_details(user: str, detail: str = "ALL"):
    if user+".mups.mfc" in get_users_list():
        profile_path = os.path.join(folder.root(), "_system_.fld", "users", user+".mups.mfc")
        if os.path.exists(profile_path):
            actions = {
                "name": file.read(profile_path, "miranda.user.profile", "name"),
                "date": file.read(profile_path, "miranda.user.profile", "date_created"),
                "unknown": file.read(profile_path, "miranda.user.profile", "unknown"),
            }
            if detail in actions:
                return actions[detail]
        else:
            print(":: Profile doesn't exists.")
    else:
        print(":: Profile doesn't exists.")


def get_user_policies(user: str, policy: str = "all") -> dict or str or None:
    policy = policy.lower()
    if user + ".mups.mfc" in get_users_list():
        profile_path = os.path.join(folder.root(), "_system_.fld", "users", user + ".mups.mfc")
        if os.path.exists(profile_path):
            if policy == "all":
                return file.read_section(profile_path, "miranda.user.policies", "py")
            else:
                if policy in file.read_section(profile_path, "miranda.user.policies", "py"):
                    return file.read_section(profile_path, "miranda.user.policies", "py")[policy]
                else:
                    print(":: Policy doesn't exists.")
        else:
            print(":: Profile doesn't exists.")
    else:
        print(":: Profile doesn't exists.")

