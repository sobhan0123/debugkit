from ..style.colors import *
from ..utils.runtime import get_caller_info


def trace(msg=""):
    info = get_caller_info()

    print(
        f"{BLUE}[TRACE]{RESET} {msg} "
        f"{GREY}({info['file']}:{info['line']}){RESET}"
    )
