import os
from _io import TextIOWrapper

byte = "byte", "b"
kilobyte = "kilobyte", "kb"
megabyte = "megabyte", "mb"
gigabyte = "gigabyte", "gb"

list_extensions = [byte, kilobyte, megabyte, gigabyte]
dict_extensions = {
    "byte": byte,
    "kilobyte": kilobyte,
    "megabyte": megabyte,
    "gigabyte": gigabyte,
    "b": byte,
    "kb": kilobyte,
    "mb": megabyte,
    "gb": gigabyte,
}

class NoContentError(Exception): pass

def get_line_by_size(file: TextIOWrapper, show_type: bool = False, linux: bool = False):
    try:
        file.seek(0)
        file_content = file.read()
    except:
        raise FileNotFoundError("Given file doesn't exist or the file path is wrong.")
    if file_content == "":
        raise NoContentError(f"Given file doesn't have any contents (empty).")
    lines = len(file_content.splitlines())
    size = os.path.getsize(file.name)
    if not show_type:
        return lines
    else:
        if linux:
            if size < 1024:
                return f"{size} Byte(s)"
            elif size < 1024 * 1024:
                return f"{size / 1024:.2f} Kilobyte(s)"
            elif size < 1024 * 1024 * 1024:
                return f"{size / (1024 * 1024):.2f} Megabyte(s)"
            else:
                return f"{size / (1024 * 1024 * 1024):.2f} Gigabyte(s)"
        else:
            if size < 1000:
                return f"{size} Byte(s)"
            elif size < 1000 * 1000:
                return f"{size / 1000:.2f} KB"
            elif size < 1000 * 1000 * 1000:
                return f"{size / (1000 * 1000):.2f} MB"
            else:
                return f"{size / (1000 * 1000 * 1000):.2f} GB"

def get_size_by_charactor(file_or_char, show_type: bool = False, linux: bool = False):
    try:
        if isinstance(file_or_char, TextIOWrapper):
            size = os.path.getsize(file_or_char.name)
        else:
            size = file_or_char
    except:
        raise FileNotFoundError(f"Given file doesn't exist or the file path is wrong.")

    if size == 0:
        raise NoContentError("Given file doesn't have any contents (empty).")

    if not show_type:
        return size

    if linux:
        if size < 1024:
            return f"{size} Byte(s)"
        elif size < 1024 * 1024:
            return f"{size / 1024:.2f} Kilobyte(s)"
        elif size < 1024 * 1024 * 1024:
            return f"{size / (1024 * 1024):.2f} Megabyte(s)"
        else:
            return f"{size / (1024 * 1024 * 1024):.2f} Gigabyte(s)"
    else:
        if size < 1000:
            return f"{size} Byte(s)"
        elif size < 1000 * 1000:
            return f"{size / 1000:.2f} KB"
        elif size < 1000 * 1000 * 1000:
            return f"{size / (1000 * 1000):.2f} MB"
        else:
            return f"{size / (1000 * 1000 * 1000):.2f} GB"

def is_binary(path: str):
    with open(path, "rb") as f:
        chunk = f.read(1024)
        if b'\0' in chunk:
            return True

    non_printable = sum(1 for byte in chunk if byte < 32 and byte not in [9, 10, 13])
    return non_printable / len(chunk) > 0.30
