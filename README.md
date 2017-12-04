Trabalho de Projeto e Análise de Algoritmos - Turma A

Alunos:
  Solon Yukio Shibata Meira   551856
  Welliton Altimari           619868

Tema: Pathfinding Algorithm

      O grupo se propôs a desenvolver soluções para o Pathfinding Problem, no qual,
    dado um labirinto, o algoritmo deve propor uma saída para ele, se tal caminho
    existir.

      Para solucionar o problema, duas abordagens foram utilizadas:
          . Recursão (Busca em profundidade);
          . Heurística A* (Utilização de função heurística para melhores palpites)

      Na solução mais simples, utilizamos a técnica de recursividade para implementar
    uma busca em profundidade, e encontrar uma saída do labirinto. Essa solução não
    necessariamente encontra o melhor caminho, mas, se houver uma saída, ela a encon-
    trará.
      Na solução utilizando o algoritmo A* modificado, a ideia é utilizar de valores já
    calculados, além de um dado pré-estabelecido (função heurística que utiliza distância
    euclidiana), para que sempre seja feita a melhor escolha do caminho a ser percorrido.
    Dessa forma, encontrando-se um caminho de saída, sabe-se que ela será a solução ótima
    do problema.
      Para esta segunda solução, o dado pré-estabelecido é que sempre a diagonal principal
    terá maior prioridade nas escolhas (peso menor).


Execução:

      Estão presentes nesta pasta dois arquivos .py, sendo eles pathfinder_Profundidade.py e
    pathfinder_astar.py. Para que seja possível executar os arquivos, é necessário instalar
    a biblioteca PyGame. O comando que deve ser executado na linha de comando para instalar
    a biblioteca no Windows é:

            . python3 -m pip install pygame --user

      Após instalada a biblioteca, os dois arquivos Python podem ser executados normalmente
    através do interpretador Python instalado na máquina.
