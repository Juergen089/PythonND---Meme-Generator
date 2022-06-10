""" Module with the abstract ingestor interface class 
as parent for the ingestors"""
from abc import ABC
from abc import abstractmethod
import string
from typing import List
from .QuoteModel import QuoteModel


class IngestorInterface(ABC):
    """Abstract class to inherit parsing files."""

    allowed_extension = ''

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """can_ingest Method checks the extension:

        Arguments:
            path -- path of the quote file as string

        Returns:
            file type can be parsed as boolean
        """
        ext = path.split('.')[-1]
        return ext == cls.allowed_extension

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Abstract method to be implemented in child classes.

        Arguments:
            path -- path of the quote file as string

        Returns:
            A list of QuoteModels with the parsed quotes of the file
        """
        pass

    @classmethod
    def get_extension(cls, path:str) -> string:
        """Return the file extension from path string.

        Arguments:
            path -- path to the file as string

        Returns:
            extension of the file as string
        """
        return path.split('.')[-1]
