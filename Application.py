import streamlit as st
import os
import subprocess
from HyDE_Implementation import generate_final_prompt
from vector_space_creation import create_vector_embeddings

def run_vector_space_creation(chunk_size, overlap_size):
    # Pass chunk_size and overlap_size as environment variables
    env = os.environ.copy()
    env["CHUNK_SIZE"] = str(chunk_size)
    env["OVERLAP_SIZE"] = str(overlap_size)

    # Run the vector_space_creation.py script
    result = subprocess.run(["python", "vector_space_creation.py"], capture_output=True, text=True, env=env)
    return result.returncode == 0 and os.path.exists("vector_embeddings.csv")


def main():
    st.set_page_config(page_title="Llama 2 Chatbot", page_icon="🐑")

    # Initialize session state variables if they do not exist
    if "api_key" not in st.session_state:
        st.session_state.api_key = ""
    if "step" not in st.session_state:
        st.session_state.step = 1
    if "temperature" not in st.session_state:
        st.session_state.temperature = 0.1
    if "top_p" not in st.session_state:
        st.session_state.top_p = 0.9
    if "max_length" not in st.session_state:
        st.session_state.max_length = 120
    if "model_ready" not in st.session_state:
        st.session_state.model_ready = False
    if "vector_space_created" not in st.session_state:
        st.session_state.vector_space_created = False
    if "chunk_size" not in st.session_state:
        st.session_state.chunk_size = 512
    if "overlap_size" not in st.session_state:
        st.session_state.overlap_size = 50

    if st.session_state.step == 1:
        st.markdown("# 🐑 Llama 2 Chatbot")
        st.markdown("## Enter your OpenAI API Key")
        api_key = st.text_input("API Key", type="password")
        if st.button("Submit"):
            st.session_state.api_key = api_key
            st.rerun()  # Reload the page to update the state

        if st.session_state.api_key and not st.session_state.vector_space_created:
            st.markdown("## Set Chunk and Overlap Size")
            chunk_size = st.slider(
                "Chunk Size",
                min_value=128,
                max_value=1024,
                value=st.session_state.chunk_size,
                step=64
            )
            overlap_size = st.slider(
                "Overlap Size",
                min_value=0,
                max_value=256,
                value=st.session_state.overlap_size,
                step=16
            )
            create_vector_placeholder = st.empty()  # Placeholder for "Create Vector Space" button
            if create_vector_placeholder.button("Create Vector Space"):
                create_vector_placeholder.empty()  # Remove the button and associated text
                create_vector_embeddings(chunk_size, overlap_size)
                if run_vector_space_creation(chunk_size, overlap_size):
                    st.session_state.vector_space_created = True
                    st.session_state.step = 2
                    st.rerun()
                else:
                    st.error("Failed to create vector space. Please try again.")

    elif st.session_state.step == 2:
        st.markdown("# Vector Space Successfully Created 🎉🎉🎉")
        st.markdown("## Set the hyperparameters of your model") 

        temperature = st.slider(
            "Temperature",
            min_value=0.01,
            max_value=1.0,
            value=st.session_state.temperature,
            step=0.01
        )

        top_p = st.slider(
            "Top_p",
            min_value=0.01,
            max_value=1.0,
            value=st.session_state.top_p,
            step=0.01
        )

        max_length = st.slider(
            "Max_length",
            min_value=32,
            max_value=128,
            value=st.session_state.max_length,
            step=1
        )

        if st.button("Set Hyperparameters"):
            st.session_state.temperature = temperature
            st.session_state.top_p = top_p
            st.session_state.max_length = max_length
            st.session_state.model_ready = True
            st.session_state.step = 3
            st.rerun()

    elif st.session_state.step == 3:
        st.markdown("## Your model is ready to use 🎉🎉🎉!")
        st.header("Models and parameters")
        st.write(f"Temperature: {st.session_state.temperature}")
        st.write(f"Top_p: {st.session_state.top_p}")
        st.write(f"Max_length: {st.session_state.max_length}")

        st.markdown("## How may I assist you today?")
        user_input = st.text_input("Your message", "")
        final_prompt = generate_final_prompt(user_input)
        st.write(final_prompt)
        if user_input:
            # Add your code to handle user input and generate responses using the Llama2 model
            st.write("Response: This is a placeholder for the chatbot's response.")
if __name__ == "__main__":
    main()