import os
import chromadb
from sentence_transformers import SentenceTransformer

print("Cargando modelo de embeddings...")

model = SentenceTransformer("all-MiniLM-L6-v2")

print("Inicializando ChromaDB persistente...")
client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_or_create_collection("docs")

docs_folder = "data/docs"

documents = []
ids = []

print("Leyendo documentos...")

for i, filename in enumerate(os.listdir(docs_folder)):
    if filename.endswith(".txt"):
        path = os.path.join(docs_folder, filename)

        with open(path, "r", encoding="utf-8") as f:
            text = f.read()

        documents.append(text)
        ids.append(str(i))

print(f"Documentos encontrados: {len(documents)}")

# limpiar colección antes de reinsertar
if collection.count() > 0:
    existing = collection.get()
    if existing["ids"]:
        collection.delete(ids=existing["ids"])
        print("Colección anterior borrada.")

print("Generando embeddings...")
embeddings = model.encode(documents)

print("Guardando en ChromaDB...")
collection.add(
    documents=documents,
    embeddings=embeddings.tolist(),
    ids=ids
)

print(f"Ingesta completada correctamente. Total en colección: {collection.count()}")