% Lab 12 Exercise 1.

% Exercise ai
killer(butch). % This is an identity statement about Butch, not about anyone he specifically killed
married(mia, marsellus).
dead(zed). % identity statement about Zed
kills(marsellus, X) :- givesFootMassage(X, mia). % two related directional statements 
loves(mia, X) :- goodDancer(X). % directional statement about Mia loving dancers
eats(jules, X) :- nutritious(X) ; tasty(X). % Jules will eat something if it is nutritious or tasty

nutritious(kale).
tasty(rice).

% Exercise aii
wizard(ron).
hasWand(harry).
quidditchPlayer(harry).
:- discontiguous wizard/1.
wizard(X):-  hasBroom(X),  hasWand(X).
hasBroom(X):-  quidditchPlayer(X). 
   % 1. wizard(ron) evaluates to true because the first line defines ron as a wizard.
   % 2. witch(ron) gives an error because witch() is not defined as a property.
   % 3. wizard(hermione) evaluates to false because hermione is not mentioned, so the knowledge base hasn't stored either that she's a wizard or that she has a broom and a wand.
   % 4. witch(hermione) gives an error because, again, witch() is not a property the knowledge base knows.
   % 5. wizard(harry) evaluates to true because the knowledge base knows that if a name has a broom and a wand, then they're a wizard.
   % 6. wizard(Y) lists ron and harry, because it is true that both are wizards.
   % 7. witch(Y) gives an error because it is not a property that the knowledgebase knows.

% Exercise b
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

% Exercise c
% Horn clauses offer more power in terms of relation between terms, while propositional logic offers more power in terms of individual statements being true or false. In Prolog, it doesn't typically make sense for a name to evaluate to true or false, because a name will become true or false in the case of a query.

% Exercise d
% Yes, in Prolog you can either ask about the truth of a specific query, like woman(mia), or you can ask it to tell you what would make the fact true, such as woman(X), which would give us X = mia.

