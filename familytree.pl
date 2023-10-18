/* Facts */
male(janardhan).
male(babu).
male(peter).
female(susan).
female(linda).
female(emma).

parent(janardhan, babu).
parent(janardhan, susan).
parent(linda, babu).
parent(linda, susan).
parent(babu, emma).
parent(peter, janardhan).
parent(susan, janardhan).

/* Rules */
father(X, Y) :- male(X), parent(X, Y).
mother(X, Y) :- female(X), parent(X, Y).
sibling(X, Y) :- parent(Z, X), parent(Z, Y), X \= Y.
