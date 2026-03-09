import os
import chromadb
from sentence_transformers import SentenceTransformer
from groq import Groq

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHROMA_PATH = os.path.join(BASE_DIR, "chroma_db")

# Embeddings + vector DB
embed_model = SentenceTransformer("all-MiniLM-L6-v2")
client_db = chromadb.PersistentClient(path=CHROMA_PATH)
collection = client_db.get_or_create_collection("docs")

# LLM
groq_client = Groq()

SYSTEM_PROMPT = """
Eres un asistente de primeros auxilios.
Responde solo con la información del contexto proporcionado.
No inventes información.
Responde en español, de forma breve, clara y natural.
Si el contexto no contiene la respuesta, di exactamente:
"No tengo información suficiente para responder a eso."
"""

def ask_rag(question: str) -> str:
    if collection.count() == 0:
        return "No tengo información sobre eso."

    emb = embed_model.encode([question])

    results = collection.query(
        query_embeddings=emb.tolist(),
        n_results=2
    )

    docs = results.get("documents", [[]])[0]

    if not docs:
        return "No tengo información sobre eso."

    context = "\n\n".join(docs)

    prompt = f"""
Contexto:
{context}

Pregunta del usuario:
{question}
"""

    completion = groq_client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt},
        ],
        temperature=0.2,
        max_tokens=220,
    )

    answer = completion.choices[0].message.content.strip()

    if not answer:
        return "No tengo información sobre eso."

    return answer