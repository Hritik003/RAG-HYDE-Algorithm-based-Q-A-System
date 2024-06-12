# Lex Fridman Podcast Transcript QA System

## Overview
The goal is to create an AI-based question-answering system that can provide accurate and contextually relevant answers based on the content of the Lex Fridman podcast transcripts. The system should:

1. Retrieve relevant passages from the podcast transcripts based on the user's questions.
2. Generate precise and contextually appropriate answers using the retrieved information.
3. Enhance the quality of retrieved passages and generated answers using HyDE to improve the embedding representations.

---

Here is detailed documentation from a user and a programming point of view

---

<details>
  <summary>For Programmers</summary>

  | Data Analysis and Code Explanation|
  |----------|
  | **Data Analysis** <br> **Attributes** <br> - Podcast id <br> - Guest of the podcast <br> - Topic of the podcast <br> - Transcript of the podcast<br><br> **Dimensional Analysis** <br> Number of rows - 319 <br> Avg no of characters in a podcast transcript - 118604 <br><br> **How it Works** <br> 1. **Converting each podcast transcript to tokens using a word tokenizer** <br><img width="179" alt="image" src="https://github.com/codechitti216/3D-Semantic-Segmentation/assets/135635287/424fa00b-50e8-42d1-ae46-300ba534cbaf"><br><br>2. **Converting each row of the transcript to chunks of tokens with some overlap to maintain the context with the following hyperparameters**<br><br><p>- Chunk Size <br>- Overlap Size<p> <br> <img width="494" alt="image" src="https://github.com/codechitti216/3D-Semantic-Segmentation/assets/135635287/ab713b05-3f76-4000-a43b-7b5bad9b8a5b"> <br><br> 3. **Converting each of the chunks into a vector using a word embedding model** <br> <img width="316" alt="image" src="https://github.com/codechitti216/3D-Semantic-Segmentation/assets/135635287/69d9ebfb-e01e-4e45-a135-0752fbfce4e7"> <br><br> 4. **Creating a vector space and storing it locally** <br> <img width="478" alt="image" src="https://github.com/codechitti216/3D-Semantic-Segmentation/assets/135635287/f5725f70-f3cd-432e-8dd6-82c761cc9858"> <br><br> 5. **Creating a function which will look for the top-k documents which best suit the input prompt based on indices like** <br> <img width="405" alt="image" src="https://github.com/codechitti216/3D-Semantic-Segmentation/assets/135635287/5f086651-1fac-4984-bf59-ae83f1af09b5"> <br><br> 6. **Creating a pseudo document for the input prompt to give it context using the Language Model loaded on your Local Server using LM Studio** <br> <img width="995" alt="image" src="https://github.com/codechitti216/3D-Semantic-Segmentation/assets/135635287/b3ded28e-b13b-46b0-ba85-0d73b149ae50"> <br> <img width="284" alt="image" src="https://github.com/codechitti216/3D-Semantic-Segmentation/assets/135635287/73f8a099-3e42-4009-9edc-edb1fe6ccc27"> <br><br> 7. **Fetching the top K documents with the best similarity with the vector of the pseudo document using the created function** <br> <img width="473" alt="image" src="https://github.com/codechitti216/3D-Semantic-Segmentation/assets/135635287/d7368272-76b7-4d05-8d67-63b00ccd7180"> <br><br>8.<p> **Generating a final prompt using prompt structures, input prompt and the top K documents fetched** <br><br><img width="856" alt="image" src="https://github.com/Hritik003/lex_llm/assets/135635287/dec375a4-8706-4fd0-a56e-ad3cf3c8e29c"> <br><br><img width="256" alt="image" src="https://github.com/Hritik003/lex_llm/assets/135635287/7486cf41-a808-433e-afc8-95ab9187be30">
 <p> |

</details>
<details>
  <summary>For Users</summary>

  | Data Analysis and Code Explanation|
  |----------|
  | **Step 1 - Setting up a language model on your local server**<br><br><p><strong>We will now setup the language model using LM Studio</strong><br>I Download LM Studio from [lmstudio.ai](https://lmstudio.ai/)<br><br>II Search for the model you wish to use<br><img width="685" alt="image" src="https://github.com/Hritik003/lex_llm/assets/135635287/3270b3a2-4603-4614-8379-4be7ade0af15"><br><br>III Refer to the Model Card and based on the size of the model, requirements of the model, download the best fit model<br><img width="1280" alt="image" src="https://github.com/Hritik003/lex_llm/assets/135635287/91a9e2e4-26be-4ad9-ad83-65a053c24cb0"><br><br>IV To run the downloaded model on your local server, Go to the Local Server tab and select Start Server. Then Click on the model you want to run as shown in the figure<br><img width="1280" alt="image" src="https://github.com/Hritik003/lex_llm/assets/135635287/16a1d1da-7ae4-4f48-8f9e-41e3f2266387"><br><br>As you can see, you can edit the System Prompt in the section. |
  |<p>**Step 2 - To open the Streamlit Application** <br><br>Go to the project directory and run Application.py by running <br><br>```pip install streamlit```<br>to install streamlit and <br><br>```streamlit run Application.py```<br><br>in the terminal to run the application<p>|
  |<p>**Step 3 - Entering your OpenAI API key as input** <br><br>as you run Application.py as mentioned, a new window will popup<br><br><img width="1278" alt="image" src="https://github.com/Hritik003/lex_llm/assets/135635287/d0bea8d4-b2eb-4730-b078-5afbf05b7176"><br><br>After adjusting the chunk length and the overlap size, after you click Create Vector Space, A Vector space would be created locally on your system based on the chunk length and the overlap size that youve set. <br><br>Please note that this step might take time.<br><p>|
  |<p>**Step 4 - Enter the hyperparameters to create the vector space** <br><br>After submitting the API key, you will see this<br><br><img width="131" alt="image" src="https://github.com/Hritik003/lex_llm/assets/135635287/ec73d9b7-50e1-4313-a079-6d846937c229"><br><br>```streamlit run Application.py```<br><br>in the terminal to run the application<p>|
  |<p>**Step 5 - Setting the Hyperparameters of the Language Model to create the Pseudo Document as per the HyDE Algorithm** <br><br>After the Vector Space is created, you should be able to locate vector_embeddings.csv in your project directory<br><br><img width="131" alt="image" src="https://github.com/Hritik003/lex_llm/assets/135635287/ec73d9b7-50e1-4313-a079-6d846937c229"><br>Now, when you look at the streamlit application this window must show up<br><br><img width="1280" alt="image" src="https://github.com/Hritik003/lex_llm/assets/135635287/5fa737ba-759d-416e-9e4a-6b9e059934e1"><br><br>Now, set the hyperparamters to the Language Model you loaded on LM Studio and click on **Set Hyperparameters**<p>|
  |<p>**Step 6 - Answering System portal** <br><br>After clicking **Set Hyperparameters**, you will be able to access the question answering system which will look like this.<br><br><img width="1280" alt="image" src="https://github.com/Hritik003/lex_llm/assets/135635287/635be7e1-fce8-4fc0-897b-5eb566883832"><br><br>
Enter your prompt there and wait for the response <p>|
</details>

