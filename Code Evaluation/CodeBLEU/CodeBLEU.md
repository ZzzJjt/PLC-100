```
import ast
from nltk.translate.bleu_score import sentence_bleu, SmoothingFunction

# 1. Regular BLEU Score
def calculate_bleu(reference_sentences, hypothesis_sentence):
    reference_tokenized = [ref.split() for ref in reference_sentences]
    hypothesis_tokenized = hypothesis_sentence.split()
    bleu_score = sentence_bleu(reference_tokenized, hypothesis_tokenized, smoothing_function=SmoothingFunction().method1)
    return bleu_score

# 2. Weighted n-gram BLEU (BLEUweight)
def calculate_bleuweight(reference_sentences, hypothesis_sentence, token_weights):
    reference_tokenized = [ref.split() for ref in reference_sentences]
    hypothesis_tokenized = hypothesis_sentence.split()
    score = 0
    for i, word in enumerate(hypothesis_tokenized):
        ngram_match = any([word in ref for ref in reference_tokenized])
        if ngram_match:
            score += token_weights.get(word, 1)  # Use the weight if provided, otherwise use 1
    weighted_score = score / len(hypothesis_tokenized)
    return weighted_score

# 3. AST Match (Matchast)
def ast_match(reference_code, hypothesis_code):
    ref_ast = ast.dump(ast.parse(reference_code))
    hyp_ast = ast.dump(ast.parse(hypothesis_code))
    match_score = 1 if ref_ast == hyp_ast else 0  # Simple match: 1 if ASTs are identical, 0 otherwise
    return match_score

# 4. Data Flow Match (Matchdf)
def data_flow_match(reference_code, hypothesis_code):
    ref_vars = set([node.id for node in ast.walk(ast.parse(reference_code)) if isinstance(node, ast.Name)])
    hyp_vars = set([node.id for node in ast.walk(ast.parse(hypothesis_code)) if isinstance(node, ast.Name)])
    match_score = len(ref_vars & hyp_vars) / len(ref_vars | hyp_vars) if ref_vars | hyp_vars else 0
    return match_score

# CodeBLEU Calculation
def calculate_codebleu(reference_code, hypothesis_code, reference_sentences, hypothesis_sentence, token_weights, alpha=0.25, beta=0.25, gamma=0.25, delta=0.25):
    # Calculate BLEU
    bleu = calculate_bleu(reference_sentences, hypothesis_sentence)
    
    # Calculate Weighted BLEU (BLEUweight)
    bleu_weight = calculate_bleuweight(reference_sentences, hypothesis_sentence, token_weights)
    
    # Calculate AST Match (Matchast)
    match_ast = ast_match(reference_code, hypothesis_code)
    
    # Calculate Data Flow Match (Matchdf)
    match_df = data_flow_match(reference_code, hypothesis_code)
    
    # CodeBLEU final score
    codebleu_score = alpha * bleu + beta * bleu_weight + gamma * match_ast + delta * match_df
    return codebleu_score

# Sample data for testing
reference_code = "def add(a, b): return a + b"
hypothesis_code = "def add(x, y): return x + y"

reference_sentences = ["def add a b return a + b"]
hypothesis_sentence = "def add x y return x + y"

# Define custom token weights for BLEUweight calculation
token_weights = {
    "def": 1.0,
    "add": 1.0,
    "a": 0.8,
    "b": 0.8,
    "x": 0.7,
    "y": 0.7,
    "return": 1.0,
    "+": 1.0
}

# Calculate CodeBLEU
codebleu_score = calculate_codebleu(reference_code, hypothesis_code, reference_sentences, hypothesis_sentence, token_weights)
codebleu_score
```

