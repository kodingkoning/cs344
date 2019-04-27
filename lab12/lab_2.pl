% Exercise 12.2

% Exercise ai
  food(bread).
  % 2.1
    % 1 unifies because they are identical.
    % 2 will not unify.
    % 8 unifies with X = bread.
    % 9 unifies with X = sausage, Y = bread.
    % 14 will not unify because it is not possible for: X = drink(beer), X = food(bread).


  % all:
  % pairs that unify: 1, 3, 4, 12, 13 
  % pairs that do not unify: 2, 5, 6, 10, 11, 14
  % 7 unifies if:
    % X = food(bread).
  % 8 unifies if:
    % X = bread.
  % 9 unifies if:
    % X = sausage.
    % Y = bread.

  % 2.2
   house_elf(dobby). 
   witch(hermione). 
   witch('McConagall').
   witch(rita_skeeter). 
   magic(X):-  house_elf(X). 
   magic(X):-  wizard(X). 
   magic(X):-  witch(X).

    % with the current knowledge base, only 5 evaluates without error
  % for 2, we need to specify:
  wizard(harry).

  % Prolog does unification through finding if it is possible for the two to become equal and then making them so, if they are not already.
  % To get more results that I would expect with this example, I would need house_elf, wizard, and witch to also be names.


% Exercise b
	% Inference in propositional logic does not use unification. With p -> q, if p is false, q is not necessarily false, so they are not necessarily equivalent.

% Exercise c
	% Prlog inferencing yes use resolution. This is what it is doing when it is looking for what will satisfy a variable in a query.


