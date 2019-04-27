% Exercise 12.3

% if she's a witch, we burn her
% looks like a witch
% they dressed her up like this
% she turned him into a newt
% burn(witch), wood...
% witches burn because they are made of wood
% can make bridges out of wood or stone
% wood floats
% floats: apples, small rocks, bread, cider, gravy, cherries, lead, ...
% weights the same if they both float
% if they float, she's made of wood, so she's a witch
% she does weight the same as a duck

burns(witch).
looksSame(her, witch).
turnsIntoNewt(witch, him).
:- discontiguous burns/1.
burns(wood).
madeOf(witch, wood).
burns(X) :- madeOf(X, wood).
make(bridge, wood).
make(bridge, stone).
floats(witch).
floats(wood).
floats(apple).
floats(verySmallRocks).
floats(bread).
floats(cider).
floats(gravy).
floats(cherry).
floats(lead).
floats(duck).
% other things float too, but it was hard to catch them all in the video

% I ran into some trouble here with the circlular logic that if something floated it was the same weight that something else that floated.
madeOf(X, wood) :- floats(X). 
floats(X) :- weighSame(X, duck).
weighSame(witch, Y) :- floats(Y).
:- discontiguous madeOf/2.
madeOf(X, Y) :- weighSame(X, Y).
:- discontiguous weighSame/2.
weighSame(her, duck).
isWitch(X) :- burns(X).

% query: isWitch(her).
