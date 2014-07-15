# Copyright 2008 Armin Ronacher.
# Licensed to PSF under a Contributor Agreement.

from lib2to3 import fixer_base
from lib2to3.fixer_util import touch_import
import six


class FixZip(fixer_base.BaseFix):

    BM_compatible = True
    order = "pre"

    PATTERN = """
    power< 'map'
        trailer< '('
            arglist< any+ >
        ')' >
    >
    """

    def transform(self, node, results):
        touch_import(six.u('six.moves'), six.u('zip'), node)
