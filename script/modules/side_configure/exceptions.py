from typing import NoReturn


class Error(Exception):
    """This is the underlying error for this package."""
    pass


class FileWriteError(Error):
    """This error occurs when data cannot be written to the file."""

    def __init__(self, file_name: str) -> NoReturn:
        self.file = file_name

    def __str__(self) -> str:
        return f"Could not write to file {self.file}"


class ArgumentsError(Error):
    def __init__(self, msg: str=None) -> NoReturn:
        self.msg = msg

    def __str__(self) -> str:
        return self.msg if self.msg is not None else 'The parameter is not correct.'
