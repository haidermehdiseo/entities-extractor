import streamlit as st
import spacy

# Define the NLP model name
MODEL_NAME = "en_core_web_lg"  # High-accuracy NLP model

# Try loading the model
try:
    nlp = spacy.load(MODEL_NAME)
except OSError:
    st.error(f"Failed to load the model '{MODEL_NAME}'. Ensure it is installed correctly.")

def extract_entities(text):
    """Extract named entities from the given text using spaCy."""
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    return entities

# Streamlit UI
st.title("Entity Extractor Tool (Named Entity Recognition)")
st.write(f"Using NLP Model: **{MODEL_NAME}**")
st.write("Paste your paragraph below, and click 'Extract Entities'.")

text_input = st.text_area("Enter your paragraph:")

if st.button("Extract Entities"):
    if text_input.strip():
        entities = extract_entities(text_input)
        if entities:
            st.subheader("Extracted Entities:")
            for entity, label in entities:
                st.write(f"**{entity}** → {label}")
        else:
            st.info("No named entities found in the text.")
    else:
        st.warning("Please enter some text first.")
