import ollama

def explain(query,item):

    prompt=f"""
Lost item description:
{query}

Found item:
{item}

Explain why this item matches.
"""

    response=ollama.chat(
        model="tinyllama",
        messages=[{"role":"user","content":prompt}]
    )

    return response["message"]["content"]