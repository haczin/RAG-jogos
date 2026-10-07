from llama_index.core.utils import set_global_tokenizer

# contador simples de palavras, porque o tiktoken está bloqueado pelo Windows
set_global_tokenizer(lambda texto: texto.split())

from llama_index.core import SimpleDirectoryReader, VectorStoreIndex, Settings
from llama_index.llms.google_genai import GoogleGenAI
from llama_index.embeddings.google_genai import GoogleGenAIEmbedding

# 1. Define os modelos: um escreve a resposta, outro transforma texto em números
Settings.llm = GoogleGenAI(model="gemini-3.5-flash-lite")
Settings.embed_model = GoogleGenAIEmbedding()

# 2. Carrega os 3 CSVs
documentos = SimpleDirectoryReader(
    input_files=["jogos.csv", "wishlist.csv", "bosses.csv"]
).load_data()

# 3. Cria o índice (aqui os textos viram embeddings)
indice = VectorStoreIndex.from_documents(documentos)

# 4. Cria o "buscador" que responde perguntas
query_engine = indice.as_query_engine()

# 5. Faz uma pergunta
resposta = query_engine.query("Quais jogos souslike aberto eu tenho?")
print(resposta)
