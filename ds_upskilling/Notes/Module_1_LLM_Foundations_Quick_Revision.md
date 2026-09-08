# Module 1 – Large Language Models (LLMs) Foundations – Quick Revision Notes

## 1. What is a Large Language Model (LLM)?
- AI model trained on massive text datasets.
- Predicts the next token in a sequence.
- Built using Transformer architecture.
- Understands context, language, and patterns.
- Foundation of ChatGPT, Claude, Gemini, Llama, etc.

## 2. Why LLMs Matter
- Natural language interaction
- Chatbots
- Code generation
- Summarization
- Translation
- Enterprise AI assistants

## 3. Evolution of LLMs
```
RNN
 ↓
LSTM
 ↓
Seq2Seq
 ↓
Attention
 ↓
Transformer
 ↓
Modern LLMs
```

## 4. Transformer Architecture
Components:
- Tokenization
- Embeddings
- Positional Encoding
- Self-Attention
- Multi-Head Attention
- Feed Forward Network
- Output Layer

## 5. Attention Mechanism
Allows the model to focus on relevant words and capture context.

## 6. Self-Attention
Every token attends to every other relevant token.

## 7. Multi-Head Attention
Different attention heads learn different relationships simultaneously.

## 8. Positional Encoding
Provides word-order information to Transformers.

## 9. Tokenization
Converts text into tokens.
Common methods:
- BPE
- WordPiece
- SentencePiece

## 10. Tokens vs Words
- Words ≠ Tokens
- API pricing is based on tokens.

## 11. Context Window
Maximum tokens processed including:
- System Prompt
- User Prompt
- Conversation History
- Retrieved Context
- Response

## 12. Embeddings
Convert text into vectors for semantic understanding.

Uses:
- Semantic Search
- RAG
- Recommendations

## 13. Cosine Similarity
Measures semantic similarity between embeddings.

## 14. Model Ecosystem
Closed:
- GPT
- Claude
- Gemini

Open:
- Llama
- Mistral
- Gemma
- Qwen
- DeepSeek
- Phi

## 15. Model Capabilities
- Text Generation
- Summarization
- Translation
- Classification
- Code Generation
- Function Calling
- Vision
- Reasoning

## 16. Hallucinations
Confident but incorrect responses.

Mitigation:
- RAG
- Better prompts
- Grounding
- Verification

## 17. Model Benchmarks
- MMLU
- HumanEval
- GSM8K
- ARC
- TruthfulQA
- HellaSwag
- SWE-Bench

## 18. Key Model Parameters

### Temperature
Controls randomness.

### Max Output Tokens
Limits response length.

### Top-k
Chooses from top K candidate tokens.

### Top-p
Chooses tokens until cumulative probability reaches P.

### Frequency Penalty
Reduces repeated words.

### Presence Penalty
Encourages new topics.

### Stop Sequences
Stops generation when a specified sequence appears.

### Seed
Improves reproducibility for testing.

### Message Roles
- System: Defines assistant behavior.
- User: User request.
- Assistant: Previous responses.

## 19. Enterprise Architecture

```
User
 ↓
System Prompt
 ↓
RAG Retrieval
 ↓
Conversation History
 ↓
LLM
 ↓
Response
```

## 20. Best Practices
- Choose the right model.
- Optimize tokens.
- Reduce hallucinations with RAG.
- Protect against prompt injection.
- Monitor latency and cost.

## 21. Interview Cheat Sheet
Know:
- LLM
- Transformer
- Self-Attention
- Tokenization
- Embeddings
- Context Window
- Benchmarks
- Temperature vs Top-p
- Frequency vs Presence Penalty
- Stop Sequences
- Seed
- Message Roles

## 22. One-Page Revision Table

| Topic | Key Takeaway |
|---|---|
| LLM | Predicts next token |
| Transformer | Uses attention |
| Tokenization | Converts text to tokens |
| Embeddings | Vector representation |
| Context Window | Max tokens processed |
| Hallucination | Incorrect confident output |
| Temperature | Randomness |
| Top-p | Dynamic sampling |
| Top-k | Fixed candidate sampling |
| Frequency Penalty | Reduce repetition |
| Presence Penalty | Encourage new ideas |
| Stop Sequences | End generation |
| Seed | Reproducibility |
| System Role | Behavior |
| User Role | Request |
| Assistant Role | Conversation context |
