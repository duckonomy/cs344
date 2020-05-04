%%%% Lab12 Exercise 1
%%%% Ian Park

%%% a. From LPN!

%% i. Exercise 1.4 - Explain why you built the representations as you did. 
% Identity of butch
killer(butch).

% Identity of mia and marsellus
married(mia, marsellus).

% Identity of zed
dead(zed).

% Relation between those marsellus kills and those who got a footmassage from mia
kills(marsellus, X):- footMassage(X, mia).

% Relation between those who mia loves and those who are good dancers
loves(mia, X):- goodDancer(X).

% Relation between those that jules eats and those that aree tasty or nutritious
eats(jules, X):- nutritious(X); tasty(X).

%% ii. Exercise 1.5 - Explain how Prolog comes up with its answers. 
wizard(ron).
hasWand(harry).
quidditchPlayer(harry).
wizard(X):-  hasBroom(X),  hasWand(X).
hasBroom(X):-  quidditchPlayer(X).

% True because ron is defined as a wizard.
wizard(ron).

% Error because witch is not defined in the knowledge base.
% witch(ron).

% False because hermione is not in the knowledge base.
wizard(hermione).

% Error because witch is not defined in the knowledge base.
% witch(hermione).

% True because harry has a wand and a broom. So from that, prolog can deduce that he is a wizard.
wizard(harry).

% Lists harry and ron because both have true values as wizards.
wizard(Y).

% Error because witch is not defined in the knowledge base.
witch(Y).

%%% b. 
% Q. Consider the well-known modus ponens. Does Prolog implement a version of modus ponens in propositional logic form? If so, demonstrate how it’s done; if not, explain why not. If it doesn’t, can you implement one? Why or why not?
% A. As we can see from the example above about wizard(harry) being true, Prolog does deduce the statement with modus ponens (p implies q; p is true; then q is true). Harry has a wand and is a quidditch player. A wizard has a broom and has a broom. A quidditch player has a broom. Thus, harry is a wizard.

hasWand(harry).
quidditchPlayer(harry).
wizard(X):-  hasBroom(X),  hasWand(X).
hasBroom(X):-  quidditchPlayer(X).

wizard(harry). % True

%%% c.
% Q. Prolog supports representations in the form of Horn clauses. Compare and contrast the representational power they provide with that of propositional logic.
% A. Horn clauses have more representational power in showing the relationship between clauses compared to propositional logic. On the other hand propositional logic is mainly using simple declarative propositions that are either true or false. This gives you more flexibility in terms of representation of individual establishments with Horn clauses.

%%% d.
% Q. Logical implementations generally distinguish the basic operations of TELL and ASK. Does Prolog support this distinction? If so, how; if not, why not? 
% A. Prolog does support this distiction. You can ASK about a query like wizard(ron), and you can make it TELL what would make the operation true by wizard(Y), which will TELL your the appropriate answer.
