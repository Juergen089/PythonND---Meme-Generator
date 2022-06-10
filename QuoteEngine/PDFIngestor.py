"""Module with the DocIngestor class to read quotes from a doc file"""
import subprocess
import random
import os
import shlex
from typing import List
from .TextIngestor import TXTIngestor
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class PDFIngestor(IngestorInterface):
    """Class to parse a pdf file with quotes"""

    allowed_extension = 'pdf'

    @classmethod
    def parse(cls, path:str) -> List[QuoteModel]:

        """method that parses the pdf file given in path
        into quotes represented by QuoteModels objects

        Arguments:
            path -- path of the pdf file to be parsed as string

        Returns:
            list of QuoteModel objects
        """

        list_of_quotes = []
        if not cls.can_ingest(path):
            raise Exception('file type cannot be ingested')
        tmp = f'./{random.randint(0,1000000)}.txt'
        cmd = f"pdftotext -layout -nopgbrk {path} {tmp}"
        args = shlex.split(cmd)
        call = subprocess.call(args)
        if call:
            raise RuntimeError("Subprocess 'pdftotext' did not return successfully.")
        list_of_quotes = TXTIngestor.parse(tmp)
        os.remove(tmp)
        return list_of_quotes