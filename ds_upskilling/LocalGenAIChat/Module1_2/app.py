import database.database as db
from services.llm_service import chat

db.create_table()
msgs = db.load_messages()
while True:
    q = input("You: ")
    if q == "exit":
        break
    msgs.append({"role": "user", "content": q})
    db.save("user", q)
    a = chat(msgs)
    print("Assistant:", a)
    msgs.append({"role": "assistant", "content": a})
    db.save("assistant", a)
