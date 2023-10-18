% Define facts for names and dates of birth
dob(babu, '1990-05-15').
dob(srivarshan, '1985-11-20').
dob(jana, '1992-03-10').
dob(virat, '1978-09-25').
dob(rohit, '1980-07-30').

% Query to retrieve date of birth for a given person
get_dob(Name, DateOfBirth) :-
    dob(Name, DateOfBirth).

% Query to retrieve names born after a certain year
born_after(Year, Name) :-
    dob(Name, DateOfBirth),
    sub_string(DateOfBirth, 0, 4, _, YearOfBirth),
    atom_number(YearOfBirth, YearBorn),
    YearBorn > Year.
