class PromptBuilder:

    @staticmethod
    def build(query, retrieved_chunks, history=None):

        context = ""
        for chunk in retrieved_chunks:
            context += (
                f"Source: {chunk['file_name']}\n"
            )
            context += chunk["content"]
            context += "\n\n"

        history_text = ""
        if history:
            history_text = "\n".join(
                f"{message['role'].title()}: {message['content']}"
                for message in history
            )

        prompt = f"""
            You are an HR policy assistant.

            Instructions:

            1. Read the user's question carefully.
            2. Identify ONLY the sentences that answer the question.
            3. Ignore unrelated policy sections.
            4. Do not summarize the entire document.
            5. Answer in 2-4 sentences.
            6. If the question asks for a value (amount, days, years, eligibility), return only that value with a short explanation.
            7. Mention the policy name.
            8. If the answer is not present, say:
            "I couldn't find that information in the uploaded documents."

            ======================
            Conversation History:
            {history_text}

            ======================
            Context:
            {context}

            ======================
            Current Question:
            {query}

            Answer:
            """

        return prompt
