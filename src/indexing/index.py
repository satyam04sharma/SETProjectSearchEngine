from abc import ABC, abstractmethod
from typing import Iterable, Dict

from .postings import Posting

class Index(ABC):
    """An Index can retrieve postings for a term from a data structure associating terms and the documents
    that contain them."""

    
    def __init__(self):
        # Using a dictionary to store the term as the key and a list of Posting objects as the value.
        self.index: Dict[str, list[Posting]] = {}

    def add_posting(self, term: str, posting: Posting):
        """Adds a posting to the index for the specified term."""
        if term not in self.index:
            self.index[term] = []
        self.index[term].append(posting)

    def get_postings(self, term: str) -> Iterable[Posting]:
        """Retrieves a sequence of Postings of documents that contain the given term."""
        return self.index.get(term, [])

    def vocabulary(self) -> list[str]:
        """A (sorted) list of all terms in the index vocabulary."""
        return sorted(self.index.keys())