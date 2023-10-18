sum(0, 0).

% Define a recursive case where the sum of a number n is the sum of n-1 plus n.
sum(N, S) :-
    N > 0,
    M is N - 1,
    sum(M, S1),
    S is S1 + N.
