% Facts representing parent-child relationships
parent(john, susan).
parent(susan, emily).
parent(susan, james).
parent(mary, john).
parent(james, anna).

% Rules for deducing grandparent relationship
grandparent(Z, X) :-
    parent(Z, Y),
    parent(Y, X).

% Backward chaining algorithm
backchain(Goal) :-
    Goal,
    writef('Goal "%w" is true.\n', [Goal]).
backchain(Goal) :-
    rule(Goal, Premises),
    writef('Goal "%w" can be inferred from:\n', [Goal]),
    write_premises(Premises),
    nl,
    deduce_premises(Premises).

 rrule(grandparent(X, Z), [parent(X, Y), parent(Y, Z)]).

% Helper predicates
write_premises([]).
write_premises([Premise|Rest]) :-
    writef('  %w\n', [Premise]),
    write_premises(Rest).

deduce_premises([]).
deduce_premises([Premise|Rest]) :-
    backchain(Premise),
    deduce_premises(Rest).
