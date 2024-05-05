from pathlib import Path
from documents import DocumentCorpus, DirectoryCorpus
from indexing import Index, TermDocumentIndex
from text import BasicTokenProcessor, EnglishTokenStream

"""This basic program builds a term-document matrix over the .txt files in 
the same directory as this file."""

def index_corpus(corpus : DocumentCorpus) -> Index:
    
    token_processor = BasicTokenProcessor()
    vocabulary = set()
    
    for d in corpus:
        print(f"Found document {d.title}")
        # TODO:
        #   Tokenize the document's content by creating an EnglishTokenStream around the document's .content()
        #   Iterate through the token stream, processing each with token_processor's process_token method.
        #   Add the processed token (a "term") to the vocabulary set.

    # TODO:
    # After the above, next:
    # Create a TermDocumentIndex object, with the vocabular you found, and the len() of the corpus.
    # Iterate through the documents in the corpus:
    #   Tokenize each document's content, again.
    #   Process each token.
    #   Add each processed term to the index with .add_term().

if __name__ == "__main__":
   # Setting up the corpus directory
    corpus_path = Path('../')
    d = DirectoryCorpus.load_text_directory(corpus_path, ".txt")

    # Build the index over this directory
    index = index_corpus(d)

    # Implementing user input loop for term searches
    while True:
        query = input("Enter search term or type 'quit' to exit: ")
        if query == "quit":
            break
        for p in index.get_postings(query):
            print(f"Document {d.get_document(p.doc_id)} contains {query}")
