import os
import os.path
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "lib"))

import prox

print(prox.prox_get("https://www.green-japan.com/search_key/01?key=zc9dua2ci6wqmb1yftkl&keyword="))
