"""Implementation of the class QuoteModel 
to hold tha data structure for the quotes"""
class QuoteModel:
    """Class as container for the quotes"""

    def __init__(self, body:str = '', author:str = ''):        
        """Each quote has two items:
        - The body
        - The name of the author
        
        :params:
        :param body: Text of a quote.
        :param author: Author of the quote.
        """
        self.body = body
        self.author = author

    def __str__(self):
        """Returns the quote (body & author) as string"""
        return f"{self.body} - {self.author}"