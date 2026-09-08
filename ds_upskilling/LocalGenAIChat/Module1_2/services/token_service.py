import tiktoken
enc=tiktoken.get_encoding('cl100k_base')
def count_messages(messages): return sum(len(enc.encode(m['content'])) for m in messages)
