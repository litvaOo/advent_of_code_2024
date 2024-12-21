from functools import cache
from itertools import pairwise
from collections import deque

lines = []
with open("input.txt") as f:
    for line in f:
        lines.append(line.strip())


positions_code = {
    "0": [("2", "^"), ("A", ">")],
    "1": [("2", ">"), ("4", "^")],
    "2": [("0", "v"), ("1", "<"), ("3", ">"), ("5", "^")],
    "3": [("2", "<"), ("6", "^"), ("A", "v")],
    "4": [("1", "v"), ("5", ">"), ("7", "^")],
    "5": [("2", "v"), ("4", "<"), ("6", ">"), ("8", "^")],
    "6": [("3", "v"), ("5", "<"), ("9", "^")],
    "7": [("4", "v"), ("8", ">")],
    "8": [("5", "v"), ("7", "<"), ("9", ">")],
    "9": [("6", "v"), ("8", "<")],
    "A": [("0", "<"), ("3", "^")],
}
positions_keypad = {
    "^": [("A", ">"), ("v", "v")],
    "<": [("v", ">")],
    "v": [("<", "<"), ("^", "^"), (">", ">")],
    ">": [("v", "<"), ("A", "^")],
    "A": [("^", "<"), (">", "v")],
}


def bfs(u, v, g):
    q = deque([(u, [])])
    seen = {u}
    shortest = None
    res = []
    while q:
        cur, path = q.popleft()
        if cur == v:
            if shortest is None:
                shortest = len(path)
            if len(path) == shortest:
                res.append("".join(path + ["A"]))
            continue
        if shortest and len(path) >= shortest:
            continue
        for nei, d in g[cur]:
            seen.add(nei)
            q.append((nei, path + [d]))
    return res


@cache
def dfs(seq, level, keypad=False):
    g = positions_keypad if keypad else positions_code
    res = 0
    seq = "A" + seq
    for u, v in pairwise(seq):
        paths = bfs(u, v, g)
        if level == 0:
            res += min(map(len, paths))
        else:
            res += min(dfs(path, level - 1, 1) for path in paths)
    return res


print(sum(dfs(line, 25) * int(line[:3]) for line in lines))
