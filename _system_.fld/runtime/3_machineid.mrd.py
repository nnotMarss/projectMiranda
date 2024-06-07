import hashlib
import socket
import uuid
import sys, os
name = os.path.basename(__file__)
sys.path.append(os.path.join(os.getcwd(), "_system_.fld", "lib", ""))
from miranda_logger import log  # noqa
id_path = os.path.join(os.getcwd(), "_system_.fld", "libdata", "miranda", "MACHINEID.var")
with open(id_path, 'r+') as f:
    if f.read() == "" or f.read() is None or f.read() == "0":

        hostname = socket.gethostname()
        mac_address = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff)
                                for elements in range(0, 2 * 6, 2)][::-1])
        unique_string = hostname + mac_address
        f.write(hashlib.md5(unique_string.encode()).hexdigest())
log("INFO", "%s: RUNTIME 3 SUCCESSFUL" % name)
