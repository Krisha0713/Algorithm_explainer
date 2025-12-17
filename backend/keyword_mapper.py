def normalize_topic(user_input):
    text = user_input.lower().strip()

    keyword_map = {
        "dp": "dynamic programming",
        "dynamic": "dynamic programming",

        "dfs": "depth first search",
        "depth search": "depth first search",

        "bfs": "breadth first search",
        "breadth search": "breadth first search",

        "binary search tree": "binary search",
        "bst": "binary search",

        "shortest path": "dijkstra",
        "dijkstra algorithm": "dijkstra",

        "greedy": "greedy algorithm",

        "merge sort algorithm": "merge sort",
        "quick sort algorithm": "quick sort",

        "bellman": "bellman ford",
        "topo sort": "topological sort"
    }

    for key in keyword_map:
        if key in text:
            return keyword_map[key]

    return text

