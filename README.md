## Task Description:

The goal is to create an AI-based question-answering system that can provide accurate and contextually relevant answers based on the content of the Lex Fridman podcast transcripts. The system should:
 
 1. Retrieve relevant passages from the podcast transcripts based on the user's questions.
    
 2. Generate precise and contextually appropriate answers using the retrieved information.
    
 3. Enhance the quality of retrieved passages and generated answers using HyDE to improve
	the embedding representations.


# Analysis of the DATA

## **Attributes**

- Podcast id
- Guest of the podcast
- Topic of the podcast
- Transcript of the podcast

Analysis of the Dimensions of the Data

- Number of rows - 319
- Average number of characters in a podcast transcript -  118604

# Steps to setup the Answering System
## Step 1 - Setting up a language model on your local server

  
**We will now setup the language model using LM Studio**

### I
Download LM Studio from [lmstudio.ai](https://lmstudio.ai/)

### II
Search for the model you wish to use 


<img width="685" alt="image" src="https://github.com/Hritik003/lex_llm/assets/135635287/3270b3a2-4603-4614-8379-4be7ade0af15">


### III
Refer to the Model Card and based on the size of the model, requirements of the model, download the best fit model 


<img width="1280" alt="image" src="https://github.com/Hritik003/lex_llm/assets/135635287/91a9e2e4-26be-4ad9-ad83-65a053c24cb0">

### IV
To run the downloaded model on your local server, 

Go to the Local Server tab and select Start Server. Then Click on the model you want to run as shown in the figure

<img width="1280" alt="image" src="https://github.com/Hritik003/lex_llm/assets/135635287/16a1d1da-7ae4-4f48-8f9e-41e3f2266387">

As you can see, you can edit the System Prompt in the section. 
 

## Step 2 - To open the Streamlit Application 

Go to the project directory and run Application.py by running


```
pip install streamlit
```
to install streamlit and 
```
streamlit run Application.py

```
in the terminal to run the application

## Step 3 - Entering your OpenAI API key as input

as you run Application.py as mentioned, a new window will popup

<img width="1278" alt="image" src="https://github.com/Hritik003/lex_llm/assets/135635287/d0bea8d4-b2eb-4730-b078-5afbf05b7176">

You should enter your OpenAI API Key and submit it

## Step 4 - Enter the hyperparameters to create the vector space

After submitting the API key, you will see this

<img width="1280" alt="image" src="https://github.com/Hritik003/lex_llm/assets/135635287/cdbf2ed1-2166-492a-8d1f-5aebeff23c78">

After adjusting the chunk length and the overlap size, after you click Create Vector Space, A Vector space would be created locally on your system based on the chunk length and the overlap size that youve set. 

Please note that this step might take time.

## Step 5 - Setting the Hyperparameters of the Language Model to create the Pseudo Document as per the HyDE Algorithm

After the Vector Space is created, you should be able to locate vector_embeddings.csv in your project directory

<img width="131" alt="image" src="https://github.com/Hritik003/lex_llm/assets/135635287/ec73d9b7-50e1-4313-a079-6d846937c229">

Now, when you look at the streamlit application this window must show up

<img width="1280" alt="image" src="https://github.com/Hritik003/lex_llm/assets/135635287/5fa737ba-759d-416e-9e4a-6b9e059934e1">

Now, set the hyperparamters to the Language Model you loaded on LM Studio and click on **Set Hyperparameters**


## Step 6 - Answering System portal

After clicking **Set Hyperparameters**, you will be able to access the question answering system which will look like this. 

<img width="1280" alt="image" src="https://github.com/Hritik003/lex_llm/assets/135635287/635be7e1-fce8-4fc0-897b-5eb566883832">


Enter your prompt there and wait for the response 
