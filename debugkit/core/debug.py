import inspect
import datetime
import psutil

from ..style.colors import CYAN, YELLOW, GREEN, GREY, RESET


def debug(*args, **kwargs):
    frame = inspect.currentframe().f_back
    info = inspect.getframeinfo(frame)

    path = info.filename.split("\\")[-1]
    line = info.lineno
    time = datetime.datetime.now().strftime("%H:%M:%S")
    mem = psutil.Process().memory_info().rss / (1024 * 1024)

    width = 40

    print(f"{CYAN}╭─ DEBUG " + "─" * (width - 9))
    if not args and not kwargs:
        locals_dict = frame.f_locals

        for name, value in locals_dict.items():
            if name.startswith("__"):
                continue
            if name in ("debug" , "inspect" , "datetime" , "psutil"):
                continue
            print(f"{CYAN}│ {YELLOW}{name}{RESET} = {GREEN}{value}{RESET}")
    if args:
        if info.code_context:
            code_line = info.code_context[0].strip()
            inside = code_line[code_line.find("(") + 1: code_line.rfind(")")]
            names = [n.strip() for n in inside.split(",")]

            for name, value in zip(names, args):
                print(f"{CYAN}│ {YELLOW}{name}{RESET} = {GREEN}{value}{RESET}")
        else:
            for i, value in enumerate(args, start=1):
                print(f"{CYAN}│ {YELLOW}arg{i}{RESET} = {GREEN}{value}{RESET}")
    for k, v in kwargs.items():
        print(f"{CYAN}│ {YELLOW}{k}{RESET} = {GREEN}{v}{RESET}")

    print(f"{CYAN}│ {GREY}file: {path}")
    print(f"{CYAN}│ {GREY}line: {line}")
    print(f"{CYAN}│ {GREY}time: {time}")
    print(f"{CYAN}│ {GREY}memory: {mem:.2f} MB")

    print(f"{CYAN}╰" + "─" * width + f"{RESET}")
