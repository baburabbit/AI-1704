% Facts about planets
planet(mercury, rocky, small, 88, 0.39).
planet(venus, rocky, medium, 225, 0.72).
planet(earth, rocky, medium, 365, 1.00).
planet(mars, rocky, small, 687, 1.52).
planet(jupiter, gas_giant, large, 4333, 5.20).
planet(saturn, gas_giant, large, 10759, 9.58).
planet(uranus, ice_giant, medium, 30687, 19.22).
planet(neptune, ice_giant, medium, 60190, 30.05).

% Rules for categorizing planets
rocky_planet(X) :- planet(X, rocky, _, _, _).
gas_giant(X) :- planet(X, gas_giant, _, _, _).
ice_giant(X) :- planet(X, ice_giant, _, _, _).

% Rules for finding planets with certain properties
closer_to_sun(X, Y) :- planet(X, _, _, X_orbit, _), planet(Y, _, _, Y_orbit, _), X_orbit < Y_orbit.
larger_than_earth(X) :- planet(X, _, Size, _, _), Size = large.
