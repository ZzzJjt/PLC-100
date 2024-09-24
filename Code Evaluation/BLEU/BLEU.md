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


**实现自适应权重调整BLEU**

我们可以为不同的 n-gram 级别（如 1-gram、2-gram、3-gram、4-gram）动态调整权重。一般情况下，BLEU 默认使用相等的权重来计算 n-gram 精度（1-gram 到 4-gram 权重为 0.25）。为了实现自适应权重调整，可以基于句子长度、复杂度或任务特点动态调整这些权重。

1.	n-gram 权重：BLEU 指标通常为 1-gram 到 4-gram 赋予相等的权重。但在某些情况下，可能需要增加 1-gram 的权重来保证基本的词汇匹配，或者增加 4-gram 的权重来保证长词组匹配的重要性。
2.	自适应调整策略：权重调整可以根据任务需求（如在代码生成中，可能更看重高 n-gram 的匹配）或者根据生成句子和参考句子的长度差异进行调整。

```
from nltk.translate.bleu_score import sentence_bleu, SmoothingFunction

# Function to calculate BLEU score with adaptive n-gram weights
def calculate_adaptive_bleu(reference_sentences, hypothesis_sentence, ngram_weights=None):
    # Tokenize the reference and hypothesis sentences
    reference_tokenized = [ref.split() for ref in reference_sentences]
    hypothesis_tokenized = hypothesis_sentence.split()

    # If no custom weights provided, use default (0.25 for 1-gram to 4-gram)
    if ngram_weights is None:
        ngram_weights = (0.25, 0.25, 0.25, 0.25)
    
    # Calculating BLEU score with adaptive weights
    bleu_score = sentence_bleu(reference_tokenized, hypothesis_tokenized, weights=ngram_weights, smoothing_function=SmoothingFunction().method1)

    return bleu_score

# Sample data
reference_sentences = ["the cat is on the mat", "there is a cat on the mat"]
hypothesis_sentence = "the cat is on the mat"

# Example 1: Equal n-gram weights (default)
bleu_score_default = calculate_adaptive_bleu(reference_sentences, hypothesis_sentence)

# Example 2: Adaptive n-gram weights (emphasize higher n-gram matches)
# Here, we give more weight to higher n-grams like 3-gram and 4-gram
adaptive_weights = (0.1, 0.2, 0.3, 0.4)
bleu_score_adaptive = calculate_adaptive_bleu(reference_sentences, hypothesis_sentence, ngram_weights=adaptive_weights)

bleu_score_default, bleu_score_adaptive
```
