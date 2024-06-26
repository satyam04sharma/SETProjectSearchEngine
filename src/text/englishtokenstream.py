from email.generator import Generator
from typing import Iterator
from .tokenstream import TokenStream

class EnglishTokenStream(TokenStream):
    def __init__(self, source):
        """Constructs a stream over a TextIOWrapper of text"""
        self.source = source
        self._open = False

    def __iter__(self) -> Iterator[str]:
        """Returns an iterator over the tokens in the stream."""
        # The source iterator probably returns lines of text, not words.
        # Get the next line, then yield each token from it.
        # for token in self.source:
        #     for t in token.split(" "):
        #         tok = t.strip()
        #         if len(tok) > 0:
        #             yield tok
        for line in self.source.splitlines():  # Ensure it iterates over each line
            for token in line.split():  # Split each line into words
                token = token.strip()  # Strip any surrounding whitespace
                if token:  # Check if token is not empty
                    yield token
                else:
                    print(f"Skipped empty token from line: {line}")


    # Resource management functions.
    def __enter__(self):
        self.source.__enter__()

    def __exit__(self):
        if self._open:
            self._open = False
            self.source.__exit__()
