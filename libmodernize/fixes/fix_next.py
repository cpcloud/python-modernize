"""Fixer for it.next() -> advance_iterator(it)"""

# Local imports
from lib2to3 import fixer_base
from lib2to3.fixer_util import touch_import, Name, Call
import six

bind_warning = "Calls to builtin next() possibly shadowed by global binding"


class FixNext(fixer_base.BaseFix):
    BM_compatible = True
    PATTERN = """
    power< base=any+ trailer< '.' attr='next' > trailer< '(' ')' > >
    """

    order = "pre" # Pre-order tree traversal

    def transform(self, node, results):
        assert results
        base = results.get('base')
        if not base:
            return
        touch_import(None, six.u('six'), node)
        base = [n.clone() for n in base]
        base[0].prefix = six.u("")
        node.replace(Call(Name(six.u("six.advance_iterator"), prefix=node.prefix), base))
