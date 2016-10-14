#!/usr/bin/env python
from __future__ import absolute_import, unicode_literals

import os
import sys

local_py = os.path.join(os.path.dirname(__file__), "lcrsweb", "settings", "local.py")

if not os.path.exists(local_py):
    open(local_py, "w").write("from .dev import *\n")

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lcrsweb.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
