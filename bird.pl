% Facts about birds
bird(canary).
bird(penguin).
bird(sparrow).
bird(ostrich).

% Rules to determine if a bird can fly
can_fly(X) :- bird(X), \+flightless(X).

flightless(penguin).
flightless(ostrich).
