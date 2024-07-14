from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings

def create_vc(text , chunk_size = 1024 , save = True) : 

    chunks = [
        text[index : index + chunk_size]
        for index 
        in range(0 , len(text) , chunk_size)
    ]

    vc = FAISS.from_texts(
        chunks , 
        embedding = OpenAIEmbeddings(model="text-embedding-3-large")
    )

    if save : vc.save_local('main_vector_db')

    return vc