% Define facts and rules for the inference engine.

% Base case: If the goal is true, it is considered interpreted.
interpret(true) :- !.

% For conjunction (AND) of two goals.
interpret((GoalA, GoalB)) :- !,
    interpret(GoalA),
    interpret(GoalB).

% Example rules/facts to demonstrate inference.
happy(john).
studies(john).
rich(john).
likes(john, ice_cream).

% Queries to demonstrate inference.
% If John studies and is rich, he is happy.
happy(john) :- studies(john), rich(john).

% If John is happy and likes ice cream, he is a joyful person.
joyful(john) :- happy(john), likes(john, ice_cream).
