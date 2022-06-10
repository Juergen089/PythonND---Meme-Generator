"""Module with the TXTIngestor class to read quotes from a csv file"""
from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class TXTIngestor(IngestorInterface):
    """Class to parse a text file with quotes"""

    allowed_extension = 'txt'

    @classmethod
    def parse(cls, path:str) -> List[QuoteModel]:
        """method that parses the text file given in path
        into quotes represented by QuoteModels objects

        Arguments:
            path -- path of the text file to be parsed as string

        Returns:
            list of QuoteModel objects
        """
        list_of_quotes = []
        if not cls.can_ingest(path):
            raise Exception('file type cannot be ingested')
        with open(path, mode="r",encoding='utf-8-sig') as infile:
            lines = infile.readlines()

        content = [line.strip('\n\r') for line in lines]

        for item in content:
            new_text, new_author = item.split('-')
            new_quote = QuoteModel(new_text.strip(), new_author.strip())
            list_of_quotes.append(new_quote)

        return list_of_quotes