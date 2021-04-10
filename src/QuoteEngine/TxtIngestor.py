"""TxtIngestor module."""
from typing import List
import docx

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class TxtIngestor(IngestorInterface):
    """Class TxtIngestor."""

    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse file txt in a list of QuoteModel."""
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        quotes = []
        with open(path, "r") as doc:
            lines = doc.readlines()
            for line in lines:
                parse = line.replace('"', '').replace('\n', '').split(' - ')
                if len(parse) == 2:
                    new_quote = QuoteModel(parse[0], parse[1])
                    quotes.append(new_quote)

        return quotes
