import os

os.environ["LLAMA_CLOUD_API_KEY"] = "llx-R8ZKh58vmQtzBWwWkzmlVxZZaZ8L3EJbI3HeTlCQhAblO8vf"
"""
import nest_asyncio
nest_asyncio.apply()
rodar antes do parse no jupyter
"""
from llama_parse import LlamaParse # Parse para traduzir informações de pdf para texto

documentos = LlamaParse(system_prompt="markdown", parsing_instruction="This file contains text and tables. I'd like to get only the tables from the text.").load_data("resultado.pdf")

print(len(documentos))

for i, pagina in enumerate(documentos):
    with open(f"meu_pdf/pagina{i+1}.md", "w", encoding="utf-8") as arquivo:
        arquivo.write(pagina.text)