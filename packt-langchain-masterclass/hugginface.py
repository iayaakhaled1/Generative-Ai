
import requests

API_URL = "https://router.huggingface.co/novita/v3/openai/chat/completions"
headers = {
    "Authorization": "Bearer token_value",
}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

response = query({
    "messages": [
        {
            "role": "user",
            "content": "What is the newest llm model?"
        }
    ],
    "max_tokens": 512,
    "model": "meta-llama/llama-3-8b-instruct"
})

# # print(response["choices"][0]["message"]["content"])

# content = response["choices"][0]["message"]["content"]
# for line in content.split("\n"):
#     print(line)




from PyPDF2 import PdfReader


pdf_path = "/workspaces/Generative-Ai/packt-langchain-masterclass/new_llm_models.pdf"

# reader = PdfReader(pdf_path) 
# print(reader)


from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter

# Step 1: Extract text from the PDF
def extract_text_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    combined_text = ''
    for i, page in enumerate(reader.pages):
        text = page.extract_text()
        if text:  # Ensure the text is not None
            combined_text += text
    return combined_text

# Step 2: Split the extracted text into chunks
def split_text_into_chunks(text):
    text_splitter = CharacterTextSplitter(
        separator="\n",  # You can adjust the separator based on your use case
        chunk_size=200,  # Adjust chunk size as needed
        chunk_overlap=20,  # Overlap for context continuity
        length_function=len
    )
    return text_splitter.split_text(text)


# Extract and split text
pdf_content = extract_text_from_pdf(pdf_path)
print("Extracted Content:")
print(pdf_content)  # Optional: Print the raw extracted content

chunked_text = split_text_into_chunks(pdf_content)
print("Split Text Chunks:")
print(chunked_text)  # Print split text chunks for verification

# The chunked text can now be used for your model queries or further processing


from sentence_transformers import SentenceTransformer
from langchain.vectorstores import FAISS
from langchain.chains import load_qa_chain

# Use a free model from sentence-transformers (e.g., all-MiniLM-L6-v2)
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")  # This is a free model


# Generate embeddings using the free model
embeddings = [embedding_model.encode(text) for text in chunked_text]

# Use FAISS for similarity search
documentSearch = FAISS.from_texts(chunked_text, embeddings)

# Question-answering chain (modify based on your QA implementation)
chain = load_qa_chain(chain_type="stuff")  # Replace OpenAI-based chains if needed
our_query = "what is the new llm model by openaI?" 
docs = documentSearch.similarity_search(our_query)

# Example to run the chain (use your implementation here)
answer = chain.run(input_documents=docs, question=our_query)
print(answer)
