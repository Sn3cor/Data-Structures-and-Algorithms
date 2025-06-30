'''
Problem dwoje kierowców
graf reprezentuje siec ulic miedzy miastami
wagi to dlugosc drogi
Znalezc taka sciezke zeby jeden kierowca przejechal jak najmniej



rozmnazamy wierzcholki na 2 casey - kto zaczyna w danym mieście i łączymy krawędziami
jak jedzie kierowca 1 to krawedz ma wage oryginalna
jak jedzie kierowca 2 to krawedz ma wage 0
dodac jeszcze dodatkowe wierzchołki
potencjalnie dodawac skierowane krawedzie

v' = 2*V+2
e' = 4*E+4

potem dijkstra lub bellman-ford
'''