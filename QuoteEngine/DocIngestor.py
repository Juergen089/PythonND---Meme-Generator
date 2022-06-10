"""Module with the DocIngestor class to read quotes from a doc file"""
import docx
from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class DocIngestor(IngestorInterface):
    """Class to parse a doc file with quotes"""

    allowed_extension = 'docx'

    @classmethod
    def parse(cls, path:str) -> List[QuoteModel]:
        """method that parses the doc file given in path
        into quotes represented by QuoteModels objects

        Arguments:
            path -- path of the doc file to be parsed as string

        Returns:
            list of QuoteModel objects
        """
        list_of_quotes = []
        document = docx.Document(path)
        if not cls.can_ingest(path):
            raise Exception('file type cannot be ingested')
        for paragraph in document.paragraphs:
            if paragraph.text != "":
                parse = paragraph.text.split('-')
                new_quote = QuoteModel(parse[0], parse[1])
                list_of_quotes.append(new_quote)

        return list_of_quotes
        