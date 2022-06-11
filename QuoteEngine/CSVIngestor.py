"""Module with the CSVIngestor class to read quotes from a csv file"""
import pandas
from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class CSVIngestor(IngestorInterface):
    """Class to parse a csv file with quotes"""

    allowed_extension = 'csv'


    @classmethod
    def parse(cls, path:str) -> List[QuoteModel]:
        """method that parses the csv file given in path
        into quotes represented by QuoteModels objects

        Arguments:
            path -- path of the text file to be parsed as string

        Returns:
            list of QuoteModel objects
        """
        if not cls.can_ingest(path):
            raise Exception('file type cannot be ingested')
        list_of_quotes = []
        df = pandas.read_csv(path, header=0)

        for index, row in df.iterrows():
            new_quote = QuoteModel(row['body'], row['author'])
            list_of_quotes.append(new_quote)

        return list_of_quotes