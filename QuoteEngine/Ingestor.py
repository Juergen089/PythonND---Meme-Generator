"""Main ingestor file"""
from typing import List
from .QuoteModel import QuoteModel
from .IngestorInterface import IngestorInterface
from .DocIngestor import DocIngestor
from .CSVIngestor import CSVIngestor
from .PDFIngestor import PDFIngestor
from .TextIngestor import TXTIngestor


class Ingestor(IngestorInterface):
    """Common ingestor class implementation"""

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse method to parse file and return quotes."""
        all_subclasses = {}
        parent = cls.__base__
        for subclass in parent.__subclasses__():
            if (subclass != cls):
                ext = subclass.allowed_extension
                all_subclasses[ext] = subclass
            
        act_ext = path.split('.')[-1]
        if (act_ext not in all_subclasses.keys()):
            raise Exception('Filetype not parsable')
        return all_subclasses[act_ext].parse(path)