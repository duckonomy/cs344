%%%% Lab12 Exercise 2
%%%% Ian Park

%%% a. From LPN! 

%% i. Exercise 2.1, questions 1, 2, 8, 9, 14 - Give the necessary instantiations. 

% Successfully unifies everytime because they are the same.
% 1. bread  =  bread

% Will not unify.
% 2. 'Bread'  =  bread 

% Will unify when X = bread.
% 8. food(X)  =  food(bread)

% Will unify when X = sausage, Y = bread.
% 9. food(bread,X)  =  food(Y,sausage) 

% Will not unify becausee you can't instatiate both X = food(bread) and X = drink(beer).
% 14. meal(food(bread),X)  =  meal(X,drink(beer)) 

%% ii. Exercise 2.2 - Explain how Prolog does its unification and reasoning. If you have issues getting the results you’d expect, are there things you can do to game the system? 
%
house_elf(dobby). 
witch(hermione). 
witch('McConagall').
witch(rita_skeeter). 
magic(X):-  house_elf(X). 
magic(X):-  wizard(X). 
magic(X):-  witch(X).

% Not satisfied
% ?-  magic(house_elf).

% Satisfied when instantiating X = harry
% ?-  wizard(harry).

% Not satisfied
% ?-  magic(wizard).

% Satisfied
% ?-  magic(’McGonagall’).

% Satisfied when instantiating X = Hermione
% ?-  magic(Hermione).

% A. Prolog does unification and reasoning through searching for possible ways to make two statements equal and making them equal. I would have to name other things as well to game the system.

%%% b
% Q. Does inference in propositional logic use unification? Why or why not?
% A. Propositional Logic lacks what First-order Logic(predicate logic) has in order to do inference with unification.

%%% c
% Q. Does Prolog inferencing use resolution? Why or why not?
% A. Yes, it does use resolution by searching the term that satisfies the variable in a query.
