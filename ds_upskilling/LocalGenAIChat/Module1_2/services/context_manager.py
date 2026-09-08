from config import MAX_CONTEXT,RESERVED_OUTPUT
from services.token_service import count_messages

def fits(messages): return count_messages(messages)<(MAX_CONTEXT-RESERVED_OUTPUT)
