# Resolução de Problemas com Grafos - Trabalhos
Repositórios para os trabalhos das aulas de Resolução de Problemas com Grafos.  

Os trabalhos são independentes, então vão ter arquivos com o mesmo nome, mas com métodos extras que foram adicionados de acordo com a necessidade.

## Como usar
Para usar o código, é necessário colocar a representação do grafo em "data.json", seguindo o exemplo dos outros que já estão no arquivo.  

O código assume que cada grafo em data.json tem a mesma estrutura, com uma chave chamada "graph" seguido de algum número que vai servir como um identificador. O valor dessa chave são outros dois valores: 
- vertices: número de vertices do grafo
- edges: array contendo as arestas do grafo (usa os índices de cada vértice como identificador, já que o trabalho não especifica um nome para eles)

Quando o grafo estiver no arquivo, basta rodar o código com o identificador do grafo como argumento ou esperar o prompt para informar o identificador.
