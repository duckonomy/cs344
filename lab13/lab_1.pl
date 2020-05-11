%! CS344 Lab13 Exercise 1
%! Ian Park
%! 05/10/2020

%%! a. Do these exercises LPN!.

%%%! i. Exercise 3.2

directlyIn(katarina, olga).
directlyIn(olga, natasha).
directlyIn(natasha, irina).

in(X, Y) :- directlyIn(X, Y).
in(X, Y) :- directlyIn(X, Z), in(Z, Y).

%%%! ii. Exercise 4.5

tran(eins,one).
tran(zwei,two).
tran(drei,three).
tran(vier,four).
tran(fuenf,five).
tran(sechs,six).
tran(sieben,seven).
tran(acht,eight).
tran(neun,nine).

listtran([],[]).
listtran([X|TX], [Y|TY]) :- tran(X, Y), listTran(TX, TY).

%%! b.

%%%! Q. Does Prolog implement a version of generalized modus ponens (i.e., modus ponens with variables and instatiation)? If so, demonstrate how it’s done; if not, explain why not. If it doesn’t, can you implement one? Why or why not? Be sure that you can explain how you built your system and how Prolog does recursion.

%%%! A. Prolog does have a version of modus ponens shown below.
satisfied(me) :- mealtomorrow(pizza).
mealtomorrow(pizza).

%%%%! This evaluates to true
%! ?- satisfied(me).
