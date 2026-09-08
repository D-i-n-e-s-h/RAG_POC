User Query
      │
      ▼
Generate Query Embedding
      │
      ▼
FAISS Search
      │
      ├───────────────┐
      ▼               ▼
Semantic Scores   BM25 Scores
      │               │
      └──────┬────────┘
             ▼
      Normalize BM25
             ▼
      Weighted Merge
             ▼
      Sort Results
             ▼
      Top-K Documents