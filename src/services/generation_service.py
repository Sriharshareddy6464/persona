import ollama


def generate_response(
        question: str,
        context: list
):

    combined_context = "\n\n".join(
        context
    )

    prompt = f"""
You are a helpful assistant.

Answer ONLY using provided context.

Question:
{question}

Context:
{combined_context}

If answer is not present,
say:

"Information not found."
"""

    response = ollama.chat(

        model="llama3",

        messages=[

            {

                "role":"user",

                "content":prompt

            }

        ]

    )

    return response["message"]["content"]