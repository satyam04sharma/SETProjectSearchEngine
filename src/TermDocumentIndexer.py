from pathlib import Path
from documents import DocumentCorpus, DirectoryCorpus
from indexing import Index, TermDocumentIndex
from text import BasicTokenProcessor, EnglishTokenStream

"""This basic program builds a term-document matrix over the .txt files in 
the same directory as this file."""

def index_corpus(corpus: DocumentCorpus) -> Index:
    token_processor = BasicTokenProcessor()
    vocabulary = set()

    for document in corpus.documents():
        print(f"Found document {document.title}")
        content = document.get_content()
        token_stream = EnglishTokenStream(content)
        for token in token_stream:
            term = token_processor.process_token(token)
            if term and term not in vocabulary:  # Filter out empty strings
                vocabulary.add(term)
                print(f"Processed term: {term}")

    index = TermDocumentIndex(vocabulary, len(corpus))
    print(f"Vocabulary built with {len(vocabulary)} terms.")

    for document in corpus.documents():
        content = document.get_content()
        token_stream = EnglishTokenStream(content)
        for token in token_stream:
            term = token_processor.process_token(token)
            if term in vocabulary:  # Only add term if it is in the vocabulary
                index.add_term(term, document.id)
                print(f"Added term '{term}' from document {document.id} to index")
            else:
                print(f"Term '{term}' not found in the initial vocabulary and will not be added.")

    return index

if __name__ == "__main__":
   # Setting up the corpus directory
    corpus_path = Path(__file__).parent.parent
    print(f"Loading documents from: {corpus_path.resolve()}")
    d = DirectoryCorpus.load_text_directory(corpus_path, ".txt")

    # Build the index over this directory
    index = index_corpus(d)

    # Implementing user input loop for term searches
    while True:
        query = input("Enter search term or type 'quit' to exit: ")
        if query == "quit":
            break
        postings = index.get_postings(query)
        if postings:
            for p in postings:
                print(f"Document {d.get_document(p.doc_id).title} contains {query}")
        else:
            print(f"No documents contain the term '{query}'.")  # This will confirm no results