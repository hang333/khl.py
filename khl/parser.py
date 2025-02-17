import shlex
from typing import Tuple, Iterable, List

from khl.message import TextMsg


def parser(msg: TextMsg, prefixes: Iterable) -> Tuple[TextMsg, List[str]]:
    for prefix in prefixes:
        if msg.content.startswith(prefix):
            try:
                raw_cmd = shlex.split(msg.content[len(prefix):])
            except ValueError:
                pass
            else:
                return msg, raw_cmd

    return msg, []
