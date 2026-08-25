# SMS Spam Classifier

A Machine Learning based SMS Spam Classifier built using Natural Language Processing (NLP) and Streamlit. The application classifies a given SMS message as either **Spam** or **Not Spam** using text preprocessing, TF-IDF feature extraction, and Machine Learning.

---

## Preview

### Prediction Example

![SMS Spam Classifier - Homepage 1](images/homepage1.png)

![SMS Spam Classifier - Homepage 2](images/homepage2.png)

---

## Features

* Classify SMS messages as Spam or Not Spam
* Natural Language Processing based text preprocessing
* Stopword removal and punctuation removal
* Porter Stemming
* TF-IDF feature extraction
* Multiple Machine Learning classification models
* Model performance comparison
* Interactive Streamlit Interface

---

## Tech Stack

* Python
* Pandas
* Scikit-learn
* NLTK
* Matplotlib
* Seaborn
* WordCloud
* Streamlit
* Pickle

---

## Dataset

* SMS Spam Dataset
* Contains Ham and Spam messages

---

## Project Workflow

1. Load the SMS dataset.
2. Remove unnecessary columns and duplicate messages.
3. Encode Ham and Spam categories.
4. Perform text preprocessing using NLTK.
5. Remove stopwords and punctuation.
6. Apply Porter Stemming.
7. Analyze the dataset using visualizations and WordClouds.
8. Convert text into numerical features using TF-IDF.
9. Train multiple Machine Learning classification models.
10. Evaluate models using Accuracy, Precision, and Confusion Matrix.
11. Compare the performance of all models.
12. Select the final model based on performance.
13. Save the trained model and TF-IDF vectorizer using Pickle.
14. Classify new SMS messages using Streamlit.

---

## Machine Learning Models

Three classification algorithms were trained and evaluated using TF-IDF features.

### 1. Multinomial Naive Bayes

* Accuracy: 97.10%
* Precision: 100.00%

Confusion Matrix:

    [[896   0]
     [ 30 108]]

### 2. Logistic Regression

* Accuracy: 95.45%
* Precision: 97.89%

### 3. Linear Support Vector Machine (SVM)

* Accuracy: 97.87%
* Precision: 97.54%

---

## Model Performance Comparison

| Model | Accuracy | Precision |
|---|---:|---:|
| Multinomial Naive Bayes | 97.10% | 100.00% |
| Logistic Regression | 95.45% | 97.89% |
| Linear SVM | 97.87% | 97.54% |

---

## Final Model

Multinomial Naive Bayes was selected as the final model.

Although Linear SVM achieved slightly higher accuracy (97.87%), Multinomial Naive Bayes achieved the highest precision (100%).

For an SMS spam classifier, high precision is important because it helps minimize legitimate messages being incorrectly classified as spam.

The final trained Multinomial Naive Bayes model was saved as:

    model.pkl

The trained TF-IDF vectorizer was saved as:

    vectorizer.pkl

---

## Project Structure

    SMS-Spam-Classifier/
    │
    ├── app.py
    ├── main.ipynb
    ├── dataset.csv
    ├── model.pkl
    ├── vectorizer.pkl
    ├── requirements.txt
    ├── README.md
    ├── .gitignore
    │
    └── images/
        ├── homepage1.png
        └── homepage2.png

---

## Installation

### Clone the repository

    git clone https://github.com/riteshmishra16/SMS-Spam-Classifier.git

### Move into the project directory

    cd SMS-Spam-Classifier

### Activate the Conda environment

    conda activate myenv

### Install the required dependencies

    pip install -r requirements.txt

---

## Run the Application

    streamlit run app.py

The application will start locally and can be accessed through the URL displayed in the terminal.

---

## Prediction

The application takes an SMS message as input and classifies it as either Spam or Not Spam.

### Example Input

    Congratulations! You have won a free prize. Click now!

### Prediction

    Spam

The application uses the saved TF-IDF vectorizer to transform the input message and the saved Multinomial Naive Bayes model to make the prediction.

---

## Future Improvements

* Improve model performance
* Add prediction probability
* Add batch SMS classification
* Improve Streamlit Interface
* Deploy the application online

---

## Author

Ritesh Kumar Mishra

GitHub: https://github.com/riteshmishra16

LinkedIn: https://www.linkedin.com/in/ritesh-kumar-mishra-234252349/