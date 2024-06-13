import pandas as pd
import openai
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

def retrieve_top_k_documents(prompt_vector, vector_database, k=5):
    chunk_vectors = [item[3] for item in vector_database]
    similarities = cosine_similarity([prompt_vector], chunk_vectors)[0]
    top_k_indices = np.argsort(similarities)[::-1][:k]
    return top_k_indices

openai.api_base = "http://localhost:1234/v1"
openai.api_key = "lm-studio"

def create_chat_completion(history):
    return openai.ChatCompletion.create(
        model="TheBloke/Llama-2-7B-Chat-GGUF",
        messages=history,
        temperature=0.7,
        stream=True,
    )

def better_prompt_generation(user_prompt):
    model_input = "Original prompt: " + user_prompt + "\n\n" + "How can we enrich this question to provide more context and depth?\n\n" + "Just give me your version of the prompt and nothing else!"
    
    system_message = (
        "You are an expert writer. Your task is to enhance the given prompt by adding more context and depth, without altering the original tone."
    )

    history = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": model_input},
    ]

    completion = create_chat_completion(history)
    new_message = {"role": "assistant", "content": ""}

    for chunk in completion:
        if 'content' in chunk.choices[0].delta:
            new_message["content"] += chunk.choices[0].delta.content

    if new_message["content"]:
        history.append(new_message)

    return new_message["content"]

def generate_final_prompt(user_prompt, vector_database_path='vector_embeddings.csv'):
    model_name_or_path = "bert-base-nli-mean-tokens"
    model = SentenceTransformer(model_name_or_path)
    output_prompt_vector = model.encode(better_prompt_generation(user_prompt))
    
    ve = pd.read_csv(vector_database_path)
    chunks_with_similarity_indices = []

    for index, row in ve.iterrows():
        vector = np.fromstring(row['chunk_vector'][1:-1], sep=' ')
        similarity = cosine_similarity(vector.reshape(1, -1), output_prompt_vector.reshape(1, -1))
        chunks_with_similarity_indices.append([similarity[0][0], row['chunk'], row['guest'], row['title']])

    chunks_with_similarity_indices.sort(reverse=True)
    chunks_with_similarity_indices = chunks_with_similarity_indices[:6]

    final_prompt = user_prompt + "\n\nAbove is the user prompt\n\n" + better_prompt_generation(user_prompt) + "\n\n Above is a better version of the prompt\n\n" "Below are the related chunks of data : \n\n"
    
    for i in chunks_with_similarity_indices:
        final_prompt +=  i[1] + "\n\n"

    final_prompt += "\n\n" + "Based on the input prompt, output prompt and the relevant chunks of data, answer the input prompt"
    
    return final_prompt 
