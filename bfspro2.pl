% Sample graph represented as facts
edge(a, b).
edge(a, c).
edge(b, d).
edge(c, d).
edge(c, e).
edge(d, e).
edge(d, f).
edge(e, f).

% bfs(Start, Goal, Path) is true if there exists a path from Start to Goal.
bfs(Start, Goal, Path) :-
    bfs_queue([[Start]], Goal, RevPath),
    reverse(RevPath, Path).

% Base case: Goal node is reached, so reverse the path.
bfs_queue([[Goal | Path] | _], Goal, [Goal | Path]).

% Recursive case: Expand the current node and add its neighbors to the queue.
bfs_queue([[Current | Path] | RestPaths], Goal, FinalPath) :-
    findall([Next, Current | Path], (edge(Current, Next), \+ member(Next, Path)), NewPaths),
    append(RestPaths, NewPaths, UpdatedQueue),
    bfs_queue(UpdatedQueue, Goal, FinalPath).

% Usage example:
% Find a path from 'a' to 'f'.
% ?- bfs(a, f, Path)
