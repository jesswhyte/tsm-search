#just trying to get the right report format

import os
import sys
import subprocess
import xml.etree.ElementTree as ET
from datetime import datetime
from hashlib import md5
from hashlib import sha1

# Import Python DFXML Bindings
# from hfs2dfxml.py 
sys.path.append('dfxml/python')
import Objects as DFXML

##
