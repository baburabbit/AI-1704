% Define the fruits and their colors
fruit_color(apple, red).
fruit_color(banana, yellow).
fruit_color(grape, purple).
fruit_color(orange, orange).
fruit_color(watermelon, green).

% Query to find the color of a specific fruit
% This will backtrack to find all possible colors for the given fruit
color_of_fruit(Fruit, Color) :-
    fruit_color(Fruit, Color).

% Query to find all fruits of a specific color
% This will backtrack to find all possible fruits for the given color
fruits_of_color(Color, Fruit) :-
    fruit_color(Fruit, Color).
