import sys
import os


def ft_tqdm(lst: range) -> None:  # type: ignore
    total = len(lst)
    try:
        bar_length = max(20, os.get_terminal_size().columns - 42)
    except (OSError, AttributeError):
        bar_length = 50

    for i, elem in enumerate(lst, 1):
        percent = int(100 * i / total)
        filled = int(bar_length * i / total)
        if filled > 0:
            bar = '=' * (filled - 1) + '>'
        else:
            bar = ''
        bar = bar.ljust(bar_length, '=')
        sys.stdout.write(f"\r{percent}%|[{bar}]| {i}/{total}")
        sys.stdout.flush()
        yield elem
