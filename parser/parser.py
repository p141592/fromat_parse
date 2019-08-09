import os
import re

from parser.exceptions import PathException
from parser.tree.nodes import Document, BlankLine, RawLine


class Parser:
    """
    Преобразование файла в объект Document
    """
    FILES_LENGTH = 0

    def __init__(self, document=None):
        self.document = Document(self.check_file(document))
        self.line = None
        self.block = None
        self.offset = 1
        self.files = []

    def check_file(self, path):
        if os.path.exists(path):
            return path
        raise PathException

    # def block_magic(func):
    #     def magic(self, line, *args, **kwargs):
    #         if line and not self.block:
    #             self.block = Block()
    #             self.document.append(self.block)
    #
    #         if not line:
    #             self.block = None
    #
    #         return func(self, line, *args, **kwargs)
    #     return magic
    #
    # @block_magic

    @staticmethod
    def check_special_symbols(line):
        if isinstance(line, BlankLine):
            return False

        reg = re.compile('[\W+^]+')
        return bool(reg.match(line.source))

    def line_magic(func):
        def magic(self, *args, **kwargs):
            line = func(self, *args, **kwargs)
            line.format_sign = self.check_special_symbols(line)
            return line
        return magic

    @line_magic
    def read_line(self, line):
        self.line = RawLine(offset=self.offset, source=line) if line else BlankLine(offset=self.offset)
        self.offset += 1
        return self.line

    def read_document(self):
        with self.document.file as f:
            for line in f.readlines():
                _line = self.read_line(line.strip('\n'))
                if _line:
                    self.document.append(_line)

        return self.document













