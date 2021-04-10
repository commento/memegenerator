"""QuoteModel module."""


class QuoteModel:
    """Class QuoteModel."""

    def __init__(self, body, author):
        """Construct a QuoteModel instance."""
        self.body = body
        self.author = author

    def __repr__(self):
        """Represent a QuoteModel instance."""
        return f'<"{self.body}" - {self.author}>'
