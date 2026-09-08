def apply(messages,n=10): return messages if len(messages)<=n else [messages[0]]+messages[-(n-1):]
