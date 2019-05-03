% Exercise 13.1
% Elizabeth Koning

% ai. 3.2
directlyIn(katarina, olga).
directlyIn(olga, natasha).
directlyIn(natasha, irina).
in(X, Y) :- directlyIn(X, Y).
in(X, Y) :- directlyIn(X, Z), in(Z, Y).

% aii 4.5
tran(eins, one).
tran(zwei, two).
tran(drei, three).
tran(vier, four).
tran(fuenf, five).
tran(sechs, six).
tran(sieben, seven).
tran(acht, eight).
tran(neun, nine).

listtran([G|X], [E|Y]) :- tran(G, E) , listtran(X, Y).
listtran([], []).


% b

% modus ponens:
  % p -> q
  % p
  % therefore q
q :- p. % p -> q
p. % p
% ?- q. % evaluate truth of q
% this implementation results in the output of q as true if we ask about the truth of q.
% however, if we do not state that q depends on p, then if we inquire about p, it gives an error instead of saying it is false.
% if we want it to volunteer the information about the implications of p being true, that's a different problem and not easy or possible to express with Prolog.
% because of the difference between propositional logic and Prolog, I do not think there is a better way to represent modus ponens.
