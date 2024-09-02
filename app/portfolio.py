import pandas as pd
import chromadb
import uuid


class Portfolio:
    def __init__(self, file_path="C:/Users/91998/Desktop/cmgt/app/resource/myportfolio1.csv - Sheet1.csv"):
        self.data = pd.read_csv(file_path,header=1)
        self.chroma_client = chromadb.PersistentClient('vectorstore')
        self.collection = self.chroma_client.get_or_create_collection(name="portfolio")

    def load_portfolio(self):
        if not self.collection.count():
            for _, row in self.data.iterrows():
                self.collection.add(documents=row["TechStack"],
                                    metadatas={"links": row["Links"]},
                                    ids=[str(uuid.uuid4())])

    def query_links(self, skills):
        return self.collection.query(query_texts=skills, n_results=2).get('metadatas', [])