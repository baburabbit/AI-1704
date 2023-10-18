% Facts
student(john).
student(mary).
student(alice).

teacher(prof_smith).
teacher(prof_jones).

subject(math, s101).
subject(english, s102).
subject(physics, s103).

% Relationships
teaches(prof_smith, math).
teaches(prof_jones, english).
teaches(prof_jones, physics).

enrolled(john, math).
enrolled(john, english).
enrolled(mary, physics).
enrolled(alice, english).

% Rules
student_subject(Student, Subject) :- enrolled(Student, SubCode), subject(Subject, SubCode).

teacher_subject(Teacher, Subject) :- teaches(Teacher, SubCode), subject(Subject, SubCode).
