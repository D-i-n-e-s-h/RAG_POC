conda activate datascience

uvicorn FastApi1:app --reload

Model:
	llama -> Open source text based AI
	llava -> Open source MultiModel AI
	

Command:
	ollama run llama3.2:3b
	python -m venv .venv -> create environment
	.venv\Scripts\activate -> activate environment
	py -3.12 -m venv .venv -> create environment with python 12
	

Package Installed:
	pip install ollama litellm tiktoken
	ollama pull nomic-embed-text
	ollama pull llama3.1:8b, ollama pull qwen3:8b
	pip install numpy



Topics:
	RAG (Retrieval-Augmented Generation)
	Embeddings -> converts text into vectors
		Sentence Transformers -> Free embedding models (all-MiniLM-L6-v2, BAAI/bge-large-en)
	Semantic Search -> search based on meaning
	Vector Databases -> ChromaDB (Free)
	AI Chat with Documents
	Knowledge Base Search

Learned:
	FIASS(Vector Database):
		IndexFlatIP -> Exact Search
		IndexIVFFlat, IndexHNSWFlat -> ANN Search
	cosine similarity:
		nearby vector search
	embedding:
		convert text to vector
	HNSW Algorithm:
		Graph based ANN search 
	Vector Database:
		internally provide option to store and search vectors
	chunking:
		paragraph/character/Recursive/Semantic/LLM based chunking for better use
		RecursiveCharacterTextSplitter (langchain) -> used to separate based on context(paragraph, line, section - all in one)
	ChromaDB:
		store and retrieve vector embeddings on query search (Bi-Encoder)
	ReRanking:
		Cross-Encoder

	

Module 6:
	Implemented:
		batch embedding(process batch of chunk at once to convert to Vector with embedding)

	To implement:
		semantic chunking(sentence-transformers/all-MiniLM-L6-v2)
		Deduplication of chunks
		Advanced Ranking Techniques
		ReRanker
		RRF
		
		
		
	
To Learn:
	Transformers
	How LLM works (not RAG)
	Hugging face


Need to consider on building RAG:
	chunking Strategies
	For code search / copilot code assistant -> use Code-aware Chunking (ATS)
	Embedding Algorithm
	Vector database based on business -> (with Hybrid search (Vector + BM25))
	Metric in semantic search in Vector Database(since semantic search default available in vector databases) (ex: cosine similarity)
	LLM Model
	ReRanking
	Multi retrieval strategy and use RRF to Rank result to send to LLM
	RAGAS -> for response evaluation	


can you provide a md file that covers module 7 all topics with 5 lines for each topics and key parameter and architecture diagram followed at last as downloadable pdf 












