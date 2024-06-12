import pandas as pd
from sentence_transformers import SentenceTransformer
import os

import os

def check_vector_embeddings_exist():
    return os.path.exists("vector_embeddings.csv")


df = pd.read_csv('podcastdata_dataset.csv')

print("Data Analysis : ")

print("There are",df['guest'].nunique(), "number of guests and", df['title'].nunique() , "number of podcasts in the dataset")


average_length_of_a_podcast = 0
temp = 0
for i in df["text"]:
  temp = temp + len(i)
average_length_of_a_podcast = temp/len(df["text"])
print("The average number of characters in a transcript of a podcast is", int(2*(average_length_of_a_podcast//2)))


new_column = []
df = df.head(2)
for i in df["text"]:
  tokens = i.split(' ')
  new_column.append(tokens)
df['tokens'] = new_column

def chunk_text(tokens, chunk_size, overlap_size, padding=True, padding_type='zero'):
    chunks = []
    start_idx = 0
    end_idx = chunk_size
    while start_idx < len(tokens):
        # Extract the current chunk
        chunk = " ".join(tokens[start_idx:end_idx])

        # Check for padding

        # Append the chunk to the list
        chunks.append(chunk)

        # Move the start and end indices for the next chunk
        start_idx += (chunk_size - overlap_size)
        end_idx = min(start_idx + chunk_size, len(tokens))

    # Padding
    if padding:
        if padding_type == 'zero':
            while len(chunks[-1]) < chunk_size:
                chunks[-1] += '0'  # Add zero-padding
        elif padding_type == 'duplicate':
            while len(chunks[-1]) < chunk_size:
                chunks[-1] += chunks[-2][-1]  # Duplicate the last token of the previous chunk
        elif padding_type == 'boundary':
            while len(chunks[-1]) < chunk_size:
                chunks[-1] += tokens[end_idx]  # Append content from the next sentence/document

    return chunks

# Example usage:
chunk_size = 1000
overlap_size = 30
new_column = []
for i in df["tokens"]:
  tokens = i
  chunks = chunk_text(tokens, chunk_size, overlap_size)
  new_column.append(chunks)
df['chunks'] = new_column


def chunk_to_vector(chunk, model_name_or_path):
    # Load the Sentence Transformers model
    model = SentenceTransformer(model_name_or_path)

    # Convert each chunk to vectors
    chunk_vector = []
    chunk_vector = model.encode(chunk)
    chunk_vector.append(chunk_vector)

    return chunk_vector



# Initialize Sentence Transformers model
model_name_or_path = "bert-base-nli-mean-tokens"
model = SentenceTransformer(model_name_or_path)

# Initialize an empty list to store vector embeddings
vector_embeddings = [["guest", "title", "chunk", "chunk_vector"]]

# Assuming df is your dataframe containing guest, title, and chunks
for index, row in df.iterrows():
    guest = row["guest"]
    title = row["title"]
    chunks = row["chunks"]

    for chunk in chunks:
        # Convert each chunk to a vector using Sentence Transformers model
        chunk_vector = model.encode(chunk)

        # Append guest, title, chunk text, and corresponding vector to vector_embeddings list
        vector_embeddings.append([guest, title, chunk, chunk_vector])

# Convert the list of lists to a pandas DataFrame
df_vector_embeddings = pd.DataFrame(vector_embeddings[1:], columns=vector_embeddings[0])

# Save the DataFrame as a CSV file
df_vector_embeddings.to_csv("vector_embeddings.csv", index=False)

