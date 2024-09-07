random_board(Board) :-
    random_permutation([1,2,3,4,5,6,7,8,9], Board).
:- dynamic(my_global_variable/1).
:- dynamic(my_global_variable1/1).
:- dynamic(my_global_variable2/1).
:- dynamic(my_global_variable3/1).
:- dynamic(my_global_variable4/1).

set_global_variable(Value) :-
    retractall(my_global_variable(_)),
    assert(my_global_variable(Value)).

get_global_variable(Value) :-
    my_global_variable(Value).

set_global_variable1(Value) :-
    retractall(my_global_variable1(_)),
    assert(my_global_variable1(Value)).

get_global_variable1(Value) :-
    my_global_variable1(Value).

set_global_variable2(Value) :-
    retractall(my_global_variable2(_)),
    assert(my_global_variable2(Value)).

get_global_variable2(Value) :-
    my_global_variable2(Value).

set_global_variable3(Value) :-
    retractall(my_global_variable3(_)),
    assert(my_global_variable3(Value)).

get_global_variable3(Value) :-
    my_global_variable3(Value).

set_global_variable4(Value) :-
    retractall(my_global_variable4(_)),
    assert(my_global_variable4(Value)).

get_global_variable4(Value) :-
    my_global_variable4(Value).

clone([],[]).
clone([H|T],[H|Z]):- clone(T,Z).


make_board(1, [_|T], NewCol, [NewCol|T]).
make_board(Row, [H|T], NewCol, [H|NewT]) :-
    Row > 1,
    NextRow is Row - 1,
    make_board(NextRow, T, NewCol, NewT).


queen_conflicts(_, [], 0, _, _).
queen_conflicts(HereCol, [OtherCol|OtherColsSet], Conflicts, HereRow, OtherRow) :-
    (   (OtherCol =:= HereCol ; abs(HereRow - OtherRow) =:= abs(OtherCol-HereCol)) ->
        (X is 1)
    ;   X is 0
    ),
    Another is OtherRow + 1,
    queen_conflicts(HereCol, OtherColsSet, Conflicts1, HereRow, Another),
    Conflicts is Conflicts1 + X.


total_conflicts([], 0, _).
total_conflicts([HereCol|OtherCols], Conflicts, HereRow) :-
    Another is HereRow +1,
    clone(OtherCols, AnotherSet),
    queen_conflicts(HereCol, OtherCols, Conflicts2, HereRow, Another),
    total_conflicts(AnotherSet, Conflicts1, Another),
    Conflicts is Conflicts1 + Conflicts2.

find_best_col(_, _, 10, _, Least, BestCol) :- 
    set_global_variable(Least),
    set_global_variable1(BestCol).


find_best_col(Row, Board, WhichCol, Confi, Least, BestCol) :-
    make_board(Row, Board, WhichCol, NewSet),
    Which is WhichCol +1,
    total_conflicts(NewSet, Conflicts, 1),
    (
        (Conflicts < Confi) ->
        NewLeast is Conflicts,
        NewBestCol is WhichCol,
        NextCol is WhichCol + 1,
        find_best_col(Row, Board, NextCol, Conflicts, NewLeast, NewBestCol)
    ; 
        find_best_col(Row, Board, Which, Confi, Least, BestCol)
    ).

find_highest_child(10,_, LeastOfLeast, BestOfBestCol, BestOfBestRow):-
    set_global_variable2(LeastOfLeast),
    set_global_variable3(BestOfBestCol),
    set_global_variable4(BestOfBestRow).



find_highest_child(Row1, Board, LeastOfLeast, BestOfBestCol, BestOfBestRow) :-
    find_best_col(Row1, Board, 1, 9, 9, 1),
    get_global_variable(Least),
    get_global_variable1(BestCol),
    (
        (Least < LeastOfLeast) ->
        NewLeast is Least,
        NewBestCol is BestCol,
        NewBestRow is Row1,
        Row2 is Row1 + 1,
        find_highest_child(Row2, Board, NewLeast, NewBestCol, NewBestRow)
    ; 
        Row2 is Row1+1,
        find_highest_child(Row2, Board, LeastOfLeast, BestOfBestCol, BestOfBestRow)
    ).
    


hill_climb([], Solution):-
    write(Solution),
    nl,
    print_board(Solution).

hill_climb(Board, Solution) :-
    total_conflicts(Board, CurConflicts, 1),
    find_highest_child(1, Board, 999, 1, 1),
    get_global_variable2(NeiConflicts),
    get_global_variable3(Col),
    get_global_variable4(Row),
    (
	(NeiConflicts < CurConflicts) ->
        make_board(Row, Board, Col, NewBoard),
        hill_climb(NewBoard, Solution)
    ;
        nl, write("NO BETTER CHOOSE "), nl,
        write("Current is "), write(CurConflicts), nl, write('neighbor is '), write(NeiConflicts), nl,
	hill_climb([], Board)
    ). 



print_board(QueenPositions) :-
    nl,
    print_board(QueenPositions, 1).


print_board(_, 10).
print_board([Column|QueenPositiget], Row) :-
    print_row(Column, Row, 1),
    nl,
    NextRow is Row + 1,
    print_board(QueenPositiget, NextRow).


print_row(_, _, 10).
print_row(Column, Row, CurrentCol) :-
    (Column =:= CurrentCol -> write('Q '); write('_ ')),
    NextCol is CurrentCol + 1,
    print_row(Column, Row, NextCol).


solve_9_queens :-
    random_board(Board),
    write(Board),
    print_board(Board),
    hill_climb(Board, Solution).


