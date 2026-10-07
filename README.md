# RAG de Jogos 🎮

Meu primeiro projeto de **RAG** (Retrieval-Augmented Generation), feito como desafio de um curso da DIO com LlamaIndex. A ideia é simples: em vez de a IA responder só com o que ela já sabe, ela consulta **os meus dados** antes de responder.

Os dados são sobre um assunto que eu conheço bem: videogames.

## O que ele faz

Eu faço uma pergunta em linguagem normal, e o programa procura nos meus arquivos os trechos mais parecidos com a pergunta. Depois, entrega esses trechos pro Gemini, que escreve a resposta.

Exemplo real:

**Pergunta:** Como eu venci o Elfo Negro?

**Resposta:** Para vencer o Elfo Negro, a estratégia utilizada foi esquivar de todos os ataques devido à dificuldade de dar parry nele, aproveitando as aberturas para bater e repetindo esse processo de esquivar e atacar até conseguir a vitória.

Essa resposta veio da estratégia que eu mesmo escrevi no arquivo de bosses. A IA não inventou nada.

## Os dados

- `jogos.csv`: jogos que eu tenho, com gênero, preço e minha nota.
- `wishlist.csv`: jogos que quero comprar, com preço e ano de lançamento.
- `bosses.csv`: chefes que enfrentei, com dificuldade e a estratégia que funcionou pra mim.

## Como funciona (por dentro)

1. **Carrega** os 3 CSVs.
2. **Transforma o texto em números** (embeddings), pra o programa conseguir medir quais linhas se parecem com a pergunta.
3. **Guarda isso num índice** em memória.
4. **Busca** os trechos mais parecidos com a pergunta.
5. **Gemini** lê esses trechos e escreve a resposta.

## Tecnologias

- Python
- LlamaIndex
- Google Gemini (modelo e embeddings)

## Como rodar

1. Crie e ative um ambiente virtual:
```
   python -m venv venv
   venv\Scripts\activate
```
2. Instale os pacotes:
```
   pip install llama-index llama-index-llms-google-genai llama-index-embeddings-google-genai
```
3. Pegue uma chave de API no [Google AI Studio](https://aistudio.google.com/apikey) e guarde no terminal (PowerShell):
```
   $env:GOOGLE_API_KEY="chave_aleatoria"
```
   A chave nunca fica escrita no código, e ela some quando o terminal é fechado.
4. Rode:
```
   python main.py
```

Pra testar outras perguntas, é só trocar o texto dentro de `query_engine.query("...")` no `main.py`.

## O que aprendi

- Como um RAG funciona de ponta a ponta, em vez de só usar pronto.
- Que o RAG é bom pra achar e resumir trechos de texto, mas não é bom pra fazer contas ou comparar tudo (tipo "qual o jogo mais caro?"), porque ele só enxerga os trechos mais parecidos com a pergunta.
- Como resolver erros reais de ambiente: Python fora do PATH, bloqueio de bibliotecas pelo Windows e mudança de modelo da API.

## Próximos passos

- [ ] Guardar o índice em disco com ChromaDB, pra não refazer os embeddings toda vez.
- [ ] Transformar em um chatbot com interface.
- [ ] Testar entrada e saída por voz.
