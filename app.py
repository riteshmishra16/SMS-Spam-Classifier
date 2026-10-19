import streamlit as st
import pickle
import string
import nltk

from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

# Ensure necessary NLTK datasets are downloaded
nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True)
nltk.download('stopwords', quiet=True)

model = pickle.load(open('model.pkl', 'rb'))
tfidf = pickle.load(open('vectorizer.pkl', 'rb'))

ps = PorterStemmer()


def transform_message(message):
    message = message.lower()
    message = nltk.word_tokenize(message)

    y = []

    for i in message:
        if i.isalnum():
            y.append(i)

    message = y[:]
    y.clear()

    for i in message:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    message = y[:]
    y.clear()

    for i in message:
        y.append(ps.stem(i))

    return " ".join(y)


st.title("SMS Spam Classifier")

input_sms = st.text_area("Enter your message")

if st.button("Predict"):

    transformed_sms = transform_message(input_sms)

    vector_input = tfidf.transform([transformed_sms])

    result = model.predict(vector_input)[0]

    if result == 1:
        st.error("Spam")
    else:
        st.success("Not Spam")