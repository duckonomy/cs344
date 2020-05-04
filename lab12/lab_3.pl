%%%% Lab12 Exercise 3
%%%% Ian Park

%%% Create a Prolog program that implements the ridiculous inferences used by Sir Bedevere (Terry Jones) to justify the burning of the witch (Connie Booth) in Monte Python's Holy Grail. Load your rules and demonstrate that the woman is indeed a witch.
witch(X):- burns(X).
burns(X):- wood(X).
wood(X):- floats(X).
floats(X):- sameWeight(X, duck).
sameWeight(girl, duck).

% ?- witch(girl).
% true
%
% ?- witch(X). 
% X = girl
