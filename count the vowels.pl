% Define the base case for an empty string (no vowels).
count_vowels("", 0).

% Define the recursive case to count vowels.
count_vowels([Char|Rest], Count) :-
    char_type(Char, alpha),  % Check if Char is an alphabet character.
    (Char = 'a' ; Char = 'e' ; Char = 'i' ; Char = 'o' ; Char = 'u' ;  % Check if Char is a vowel.
     Char = 'A' ; Char = 'E' ; Char = 'I' ; Char = 'O' ; Char = 'U'),
    count_vowels(Rest, RemainingCount),  % Recursive call for the rest of the string.
    Count is RemainingCount + 1.  % Increment the count.

% If the character is not a vowel, continue with the rest of the string.
count_vowels([Char|Rest], Count) :-
    char_type(Char, alpha),
    \+ (Char = 'a' ; Char = 'e' ; Char = 'i' ; Char = 'o' ; Char = 'u' ;
       Char = 'A' ; Char = 'E' ; Char = 'I' ; Char = 'O' ; Char = 'U'),
    count_vowels(Rest, Count).

% Ignore non-alphabet characters and continue with the rest of the string.
count_vowels([_|Rest], Count) :-
    count_vowels(Rest, Count).
