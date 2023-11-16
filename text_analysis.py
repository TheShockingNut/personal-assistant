import spacy

# Load spaCy model
nlp = spacy.load("en_core_web_sm")  # Use the appropriate spaCy model for your language

def analyze_text(text):
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    pos_tags = [(token.text, token.pos_) for token in doc]
    return entities, pos_tags