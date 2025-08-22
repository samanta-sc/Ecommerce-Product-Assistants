from langchain_astradb import AstraDBVectorStore
# from langchain_openai import OpenAIEmbeddings
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
import os
import pandas as pd
from ecommbot.data_converter import dataconverter

load_dotenv()

GOOGLE_API_KEY="AIzaSyBUidwv9u6nTYAt5erIKn2md-4yQz__-fU"
ASTRA_DB_API_ENDPOINT="https://6a5e6097-0fd7-483d-aa88-951f9c4e2560-us-east-2.apps.astra.datastax.com"
ASTRA_DB_APPLICATION_TOKEN="AstraCS:XyBYJckyGTROOyyYExkLdcGc:dd4238882abd422897a473396ee7be0a13fb7a68c76040fbca581757fad5d196"
# ASTRA_DB_KEYSPACE="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"

embedding = GoogleGenerativeAIEmbeddings(model = "models/embedding-001")

def ingestdata(status):
    vstore = AstraDBVectorStore(
            embedding=embedding,
            collection_name="chatbotecomm",
            api_endpoint=ASTRA_DB_API_ENDPOINT,
            token=ASTRA_DB_APPLICATION_TOKEN,
            # namespace=ASTRA_DB_KEYSPACE,
        )
    
    storage=status
    
    if storage==None:
        docs=dataconverter()
        inserted_ids = vstore.add_documents(docs)
    else:
        return vstore
    return vstore, inserted_ids

if __name__=='__main__':
    vstore,inserted_ids=ingestdata(None)
    print(f"\nInserted {len(inserted_ids)} documents.")
    results = vstore.similarity_search("can you tell me the low budget sound basshead.")
    for res in results:
            print(f"* {res.page_content} [{res.metadata}]")
            

   
