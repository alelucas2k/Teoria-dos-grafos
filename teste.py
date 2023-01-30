from meu_grafo_matriz_adj_dir import MeuGrafo


paraiba = MeuGrafo()

paraiba.adiciona_vertice("J")
paraiba.adiciona_vertice("C")
paraiba.adiciona_vertice("E")
paraiba.adiciona_vertice("P")
paraiba.adiciona_vertice("M")
paraiba.adiciona_vertice("T")
paraiba.adiciona_vertice("Z")

paraiba.adiciona_aresta('a1', 'J', 'C')
paraiba.adiciona_aresta('a2', 'C', 'E')
paraiba.adiciona_aresta('a3', 'E', 'C')
paraiba.adiciona_aresta('a4', 'C', 'P')
paraiba.adiciona_aresta('a5', 'P', 'C')
paraiba.adiciona_aresta('a6', 'C', 'T')
paraiba.adiciona_aresta('a7', 'C', 'M')
paraiba.adiciona_aresta('a8', 'M', 'T')
paraiba.adiciona_aresta('a9', 'T', 'Z')

paraiba.dijkstra_drone("J", "C")
