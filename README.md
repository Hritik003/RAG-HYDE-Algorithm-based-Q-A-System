## Task Description:

The goal is to create an AI-based question-answering system that can provide accurate and contextually relevant answers based on the content of the Lex Fridman podcast transcripts. The system should:
 
 1. Retrieve relevant passages from the podcast transcripts based on the user's questions.
    
 2. Generate precise and contextually appropriate answers using the retrieved information.
    
 3. Enhance the quality of retrieved passages and generated answers using HYDE to improve
	the embedding representations.



## Setup

**1.1. Environment Setup**

run in terminal the following:

```
pip install virtualenv

virtualenv rag_env


rag_env\Scripts\activate

source rag_env/bin/activate

```

**1.2. Install Necessary Libraries**
``` 
pip install -r requirements.txt
```

**1.3. Download the Dataset**

``` python 
import kaggle
kaggle.api.dataset_download_files('rajneesh231/lex-fridman-podcast-transcript', unzip=True)

```

## Data Loading

**2.1 Load the dataset**

```python
df=pd.read_csv('podcastdata_dataset.csv)
```

**2.2 Dataset**

We will use the `Lex Fridman Podcast Transcript` dataset, which contains comprehensive transcripts of conversations between Lex Fridman and his esteemed guests.
