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

