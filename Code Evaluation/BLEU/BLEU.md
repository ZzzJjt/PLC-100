```
# Importing the necessary libraries
from nltk.translate.bleu_score import sentence_bleu, SmoothingFunction

# Function to calculate BLEU score for a list of hypothesis and references
def calculate_bleu(reference_sentences, hypothesis_sentence):
    # Tokenize the reference and hypothesis sentences
    reference_tokenized = [ref.split() for ref in reference_sentences]
    hypothesis_tokenized = hypothesis_sentence.split()

    # Calculating BLEU score
    bleu_score = sentence_bleu(reference_tokenized, hypothesis_tokenized, smoothing_function=SmoothingFunction().method1)

    return bleu_score

# Sample data
reference_sentences = ["the cat is on the mat", "there is a cat on the mat"]
hypothesis_sentence = "the cat is on the mat"

# Calculate BLEU score
bleu_score = calculate_bleu(reference_sentences, hypothesis_sentence)
bleu_score
```
