#
# (c) 2024 nnotMarss / m4rs_fox / Mars-Jann Fox
#   marsFile redistributed under the MIT License
#          Details: marsfile_license.txt
#
import base64, base58, os, sys, json, time, random  # noqa
from datetime import datetime  # noqa

sys.path.append(os.path.abspath(os.path.join(os.getcwd(), *([os.pardir] * 1))))
import miranda_obfuscate  # noqa
import miranda_language as lang # noqa


class module:
    version = '2.0'
    supported = ['2.0']
    idents = [
        'sS',
        'sI',
        'sF',
        'sB',
        'sL',
        'bF',
        'bS',
        'bC'
    ]
    statuses = [
        "UNLOCKED",
        "LOCKED",
        "PERM_LOCKED"
    ]


class to_be_removed(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class errors:
    class general(Exception):
        def __init__(self, message):
            self.message = message
            super().__init__(self.message)

    class bool_invalid(Exception):
        def __init__(self, message):
            self.message = message
            super().__init__(self.message)

    class base_invalid(Exception):
        def __init__(self, message):
            self.message = message
            super().__init__(self.message)

    class syntax_invalid(Exception):
        def __init__(self, message):
            self.message = message
            super().__init__(self.message)

    class version_invalid(Exception):
        def __init__(self, message):
            self.message = message
            super().__init__(self.message)

    class file_locked(Exception):
        def __init__(self, message):
            self.message = message
            super().__init__(self.message)

    class file_not_exists(Exception):
        def __init__(self, message):
            self.message = message
            super().__init__(self.message)

    class file_exists(Exception):
        def __init__(self, message):
            self.message = message
            super().__init__(self.message)

    class file_entry(Exception):
        def __init__(self, message):
            self.message = message
            super().__init__(self.message)


class section:
    def __init__(self, name):
        self.name = name
        self.entries = []

    def add_entry(self, entry_name):
        self.entries.append(entry_name)


class entry:
    def __init__(self, ident, value):
        self.ident = ident
        self.value = value


def process_entry(ident, name, process_value, line, line_number):
    _ = line

    def str_to_bool(value):
        value = value.upper()
        if value == "TRUE":
            return True
        elif value == "FALSE":
            return False
        else:
            raise errors.bool_invalid(lang.lang(lang.current_lang(), "mars_bool_invalid") % (value, line_number))

    def base58_decode(value):
        try:
            return base58.b58decode(value).decode()
        except TypeError:
            raise errors.base_invalid(lang.lang(lang.current_lang(), "mars_base58_invalid") % (value, line_number))

    def base64_decode(value):
        try:
            return base64.b64decode(value).decode()
        except TypeError:
            raise errors.base_invalid(lang.lang(lang.current_lang(), "mars_base64_invalid") % (value, line_number))

    def code_decode(value):
        try:
            return base64_decode(base58_decode(base64_decode(value.encode())))
        except TypeError:
            raise errors.base_invalid(lang.lang(lang.current_lang(), "mars_base_invalid") % (value, line_number))

    actions = {
        'sS': lambda v: str(v),
        'sI': lambda v: int(v),
        'sF': lambda v: float(v),
        'sB': str_to_bool,
        'sL': lambda v: v.split(';'),
        'bF': base58_decode,
        'bS': base64_decode,
        'bC': code_decode,
    }

    if ident not in actions:
        raise errors.syntax_invalid(lang.lang(lang.current_lang(), "mars_id_invalid") % (ident, line_number))

    new_entry = entry(name, actions[ident](process_value))
    return new_entry


def parse(file_path_parse):
    sections = []
    current_section = None

    with open(file_path_parse, 'r') as file:
        for i, line in enumerate(file, start=1):
            line = line.strip()

            if "`" in line and not line.startswith('`'):
                raise errors.syntax_invalid(lang.lang(lang.current_lang(), "mars_comment_invalid") % (line, i))  # noqa

            elif line.startswith('`'):
                pass

            elif line.startswith("$<") and line.endswith(">"):
                if i == 1:
                    file_version = line.split('$<')[1].split('>')[0]
                    if file_version not in module.supported:
                        raise errors.version_invalid(
                            lang.lang(lang.current_lang(), "mars_support_invalid") % (
                                file_version, module.supported, module.version))
                elif i == 2:
                    pass
                else:
                    raise errors.syntax_invalid(
                        lang.lang(lang.current_lang(), "mars_tag_invalid") % (
                            line, i))

            elif line.startswith("$<") and line.endswith(">"):
                if i == 2:
                    file_status = line.split('$<')[1].split('>')[0]
                    if file_status.upper() == "UNLOCKED":
                        pass
                    elif file_status.upper() == "LOCKED" or file_status.upper() == "PERM_LOCKED":
                        raise errors.file_locked("\n---\nERROR: File is locked!\n---")
                    else:
                        raise errors.syntax_invalid("\n---\nERROR: Invalid lock tag.\n---")
                else:
                    raise errors.syntax_invalid(
                        "\n---\nERROR: Invalid lock tag position: \'%s\' in line %s. Should be 2.\n---" % i)

            elif line.startswith('['):

                if line.startswith('[e~'):
                    end_section_name = line.split('[e~')[1].split(']')[0]
                    if current_section.name == end_section_name:
                        current_section = None
                    else:
                        raise errors.syntax_invalid(
                            "\n---\nERROR: Missing/Mismatched header: \'%s\' in line %s\n---" % (
                                line, i))

                elif line.startswith('[s~'):
                    if current_section is None:
                        section_name = line.split('[s~')[1][:-1]
                        current_section = section(section_name)
                        sections.append(current_section)

            elif line.startswith('{'):
                if current_section is None:
                    raise errors.syntax_invalid("\n---\nERROR: Invalid formatting: \'%s\' in line %s\n---" % (line, i))

                ident, rest = line[1:].split('~')
                name, value = rest.split('/')
                value = value[:-1]

                current_section.add_entry(process_entry(ident, name, value, line, i))
    return sections


def read(_data_, section_name: str, entry_name: str):
    file_data = parse(_data_)
    for section__ in file_data:
        if section__.name == section_name:
            for entry__ in section__.entries:
                if entry__.ident == entry_name:
                    if entry__.value is None:
                        raise errors.syntax_invalid("\n---\nERROR: Missing entry!\n---")
                    return entry__.ident, entry__.value


def read_section(_data_, section_name: str, style: str = "both"):
    style = style.lower()
    new_dict = {}
    file_data = parse(_data_)
    for section__ in file_data:
        if section__.name == section_name:
            for entry__ in section__.entries:
                new_dict[entry__.ident] = {
                    "ident": entry__.ident,
                    "value": entry__.value,
                }
            actions = {
                "py": new_dict,
                "json": json.dumps(new_dict),
                "both": [new_dict, json.dumps(new_dict)],
            }
            if style in actions:
                return actions[style]
            else:
                return None


def status(file_path):
    if os.path.exists(file_path):
        target = open(file_path, 'r+')
        lines = target.readlines()
        for i, line in enumerate(lines):
            if i == 1 and line.strip().startswith("$"):
                return line.strip().split("$<")[1].split(">")[0]
    else:
        raise errors.file_not_exists("\n---\nERROR: File does not exist!\n---")


def overwrite(file_path: str, section_name: str, entry_name: str, new_value):
    if status(file_path) == "UNLOCKED":
        chars = None
        stop = False
        found_break = False
        found_start = [False, None]
        if "/" in new_value:
            new_value = new_value.split('/')
            new_value = "\\".join(new_value)
            chars = chars, "/"
        if "~" in new_value:
            new_value = new_value.split('~')
            new_value = "-".join(new_value)
            chars = chars, "~"
        if chars is not None:
            print(f":: Prohibited characters detected: {chars}!\n:: These were replaced with closest alternatives.")
        with open(file_path, 'r+') as file:
            lines = file.readlines()
            for i, line in enumerate(lines):
                if line.strip().startswith("[s~") and line.strip().endswith("]") and section_name in line:
                    found_start = [True, line.strip().split("~")[1].split("]")[0]] if \
                        line.strip().split("~")[1].split("]")[0] == section_name else [False, None]
                elif line.strip().startswith("[e~") and line.strip().endswith("]") and section_name in line:
                    found_break = True if line.strip().split("~")[1].split("]")[0] == section_name else False
                if found_break and found_start:
                    stop = True
                if line.strip().startswith("{") and entry_name in line:
                    if not stop and found_start[1] == section_name:
                        if line.split("~")[0][1:] == 'bS':
                            try:
                                new_value = base64.b64encode(new_value.encode())
                                lines[i] = "{%s~%s/%s}\n" % (
                                    line.split("~")[0][1:], entry_name, new_value.decode('UTF-8'))
                            except TypeError:
                                raise errors.base_invalid("\n---\nERROR: Not a valid BASE64: %s" % new_value)
                        elif line.split("~")[0][1:] == 'bF':
                            try:
                                new_value = base58.b58encode(new_value.encode())
                                lines[i] = "{%s~%s/%s}\n" % (
                                    line.split("~")[0][1:], entry_name, new_value.decode('UTF-8'))
                            except TypeError:
                                raise errors.base_invalid("\n---\nERROR: Not a valid BASE58: %s" % new_value)
                        elif line.split("~")[0][1:] == 'bC':
                            try:
                                new_value = base64.b64encode(
                                    base58.b58encode(base64.b64encode(new_value.encode()))).decode()
                                lines[i] = "{%s~%s/%s}\n" % (line.split("~")[0][1:], entry_name, new_value)

                            except TypeError:
                                raise errors.base_invalid("\n---\nERROR: Not a valid CODE: %s" % new_value)

                        elif line.split("~")[0][1:] == 'sL':
                            mars_list = ""
                            for obj in new_value:
                                mars_list = mars_list + obj + ";"  # noqa
                            lines[i] = "{%s~%s/%s}\n" % (line.split("~")[0][1:], entry_name, mars_list[:-1])
                        else:
                            lines[i] = "{%s~%s/%s}\n" % (line.split("~")[0][1:], entry_name, new_value)
            open(file_path, 'w').writelines(lines)
    elif status(file_path) == "LOCKED":
        raise errors.file_locked("\n---\nERROR: File is locked!\n---")
    elif status(file_path) == "PERM_LOCKED":
        raise errors.file_locked("\n---\nERROR: File is permanently locked!\n---")


def write(file_path: str, section_name: str, entry_name: str, value, ident: str = "sS"):
    def write_main(file_path_tmp: str, section_name_tmp: str, entry_name_tmp: str, value_tmp, ident_tmp: str = "sS"):
        value_tmp = str(value_tmp)
        chars = None
        if "/" in value_tmp:
            value_tmp = value_tmp.replace("/", "\\")
            chars = chars, "/"
        if "~" in value_tmp:
            value_tmp = value_tmp.replace("~", "-")
            chars = chars, "~"
        if chars is not None:
            print(f":: Prohibited characters detected: {chars}!\n:: These were replaced with closest alternatives.")
        with open(file_path_tmp, 'r+') as file:
            lines = file.readlines()
            section_found = False
            tracked_end = -1
            for i, line in enumerate(lines):
                if line.strip().startswith("[s~") and line.strip().endswith("]") and \
                        line.strip().split("~")[1].split("]")[0] == section_name_tmp:
                    section_found = True
                elif line.strip().startswith("[e~") and line.strip().endswith("]") and \
                        line.strip().split("~")[1].split("]")[0] == section_name_tmp:
                    tracked_end = i
                tracked_entry = line.strip().split("~")[1].split("/") if line.strip().startswith("{") else [None, None]
                if tracked_entry[0] == entry_name_tmp:
                    raise errors.file_entry("\n---\nERROR: Duplicate entry!\n---")
            if ident_tmp not in module.idents:
                raise errors.syntax_invalid("\n---\nERROR: Invalid ident_tmp!\n---")
            if not section_found:
                lines.append(f"\n[s~{section_name_tmp}]\n")
                lines.append("{%s~%s/%s}\n" % (ident_tmp, entry_name_tmp, value_tmp))
                lines.append(f"[e~{section_name_tmp}]")
                file.seek(0)
                file.writelines(lines)
                file.close()
            else:
                if tracked_end != -1:
                    lines[tracked_end] = "{%s~%s/%s}\n%s" % (ident_tmp, entry_name_tmp, value_tmp, lines[tracked_end])
                file.seek(0)
                file.writelines(lines)
                file.close()

    if status(file_path) == "UNLOCKED":
        write_main(file_path, section_name, entry_name, value, ident)
        overwrite(file_path, section_name, entry_name, value)
    elif status(file_path) == "LOCKED":
        raise to_be_removed("\n---\nERROR: File is locked!\n---")
    elif status(file_path) == "PERM_LOCKED":
        raise to_be_removed("\n---\nERROR: File is permanently locked!\n---")


def to_json(_data_, _new_, _style_=6):
    if not os.path.exists(_new_):
        open(_new_, 'w').close()
    try:
        _ = int(_style_)
    except to_be_removed:
        raise errors.syntax_invalid("\n---\nERROR: Invalid integer!\n---")
    new_data = open(_new_, 'w')
    new_dict = {}
    file_data = parse(_data_)
    for section__ in file_data:
        for entry__ in section__.entries:
            if section__.name not in new_dict:
                new_dict[section__.name] = {}
            new_dict[section__.name][entry__.ident] = {
                "ident": entry__.ident,
                "value": entry__.value,
            }
    new_data.write(json.dumps(new_dict, indent=_style_))
    return json.dumps(new_dict)


def create(file_path=".\\", file_name="newfile_%s.mfc" % random.randint(1, 10000), file_status="UNLOCKED"):
    target = os.path.join(file_path, file_name)
    if file_status in module.statuses:
        if not os.path.exists(target):
            _file = open(target, 'w')
            _file.write("$<%s>\n$<%s>\n` File created by script on %s." % (module.version, file_status, datetime.now()
                                                                           .strftime("%d-%m-%Y %I:%M:%S%p")))
            _file.close()
            time.sleep(.5)
            return target, file_name
        else:
            raise errors.file_exists("\n---\nERROR: File already exists!\n       %s\n---" % target)
    else:
        raise errors.syntax_invalid("\n---\nERROR: Invalid lock tag.\n---")


def set_status(file_path, new_status="LOCKED"):
    if os.path.exists(file_path):
        if new_status in module.statuses:
            target = open(file_path, 'r+')
            lines = target.readlines()
            for i, line in enumerate(lines):
                if i == 1 and line.strip().startswith("$"):
                    current_status = line.strip().split("$<")[1].split(">")[0]
                    if current_status != new_status and current_status != "PERM_LOCKED":
                        lines[i] = "$<%s>\n" % new_status
                    elif current_status == new_status:
                        pass
                    elif current_status == "PERM_LOCKED":
                        raise errors.file_locked("\n---\nERROR: File permanently locked!\n---")
                    else:
                        raise errors.general("\n---\nERROR: Unknown error!\n---")
            target.seek(0)
            target.writelines(lines)
            target.close()
        else:
            raise errors.syntax_invalid("\n---\nERROR: Invalid lock tag type!\n---")
    else:
        raise errors.file_exists("\n---\nERROR: File does not exist!\n---")

# this whole script was painful to code -Mars
