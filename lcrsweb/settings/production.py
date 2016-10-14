from __future__ import absolute_import, unicode_literals

from .base import *  # @UnusedWildImport

DEBUG = False

ADMINS = (
    ('Benjamin Bach', 'benjamin@fairdanmark.dk'),
)

try:
    from .local import *  # @UnusedWildImport
except ImportError:
    pass
