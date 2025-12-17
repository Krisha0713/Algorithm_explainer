def get_diagram(topic, level):
    topic = topic.lower()
    level = level.lower()

    diagrams = {

        "dynamic programming": {
            "beginner": """
            graph TD
            A[Problem] --> B[Subproblem 1]
            A --> C[Subproblem 2]
            B --> D[Store Result]
            C --> D
            """,
            "intermediate": """
            graph TD
            A[DP Table]
            A --> B[State 1]
            A --> C[State 2]
            B --> D[Reuse]
            C --> D
            """,
            "advanced": """
            graph TD
            A[T(n)]
            A --> B[T(n-1)]
            A --> C[T(n-2)]
            B --> D[Memoization]
            C --> D
            """
        },

        "divide and conquer": {
            "beginner": """
            graph TD
            A[Problem] --> B[Part 1]
            A --> C[Part 2]
            B --> D[Solution]
            C --> D
            """,
            "intermediate": """
            graph TD
            A[T(n)]
            A --> B[T(n/2)]
            A --> C[T(n/2)]
            """,
            "advanced": """
            graph TD
            A[T(n)]
            A --> B[T(n/2)]
            A --> C[T(n/2)]
            B --> D[Merge]
            C --> D
            """
        },

        "binary search": {
            "beginner": """
            graph TD
            A[Sorted Array] --> B[Middle Element]
            B --> C[Found]
            B --> D[Discard Half]
            """,
            "intermediate": """
            graph TD
            A[Low, High]
            A --> B[Mid]
            B --> C[Target Left]
            B --> D[Target Right]
            """,
            "advanced": """
            graph TD
            A[Invariant]
            A --> B[Log n Steps]
            """
        },

        "merge sort": {
            "beginner": """
            graph TD
            A[Array] --> B[Left Half]
            A --> C[Right Half]
            """,
            "intermediate": """
            graph TD
            A[Divide] --> B[Sort Left]
            A --> C[Sort Right]
            B --> D[Merge]
            C --> D
            """,
            "advanced": """
            graph TD
            A[T(n)] --> B[2T(n/2)]
            B --> C[O(n)]
            """
        },

        "quick sort": {
            "beginner": """
            graph TD
            A[Array] --> B[Choose Pivot]
            B --> C[Partition]
            """,
            "intermediate": """
            graph TD
            A[Pivot]
            A --> B[Left Partition]
            A --> C[Right Partition]
            """,
            "advanced": """
            graph TD
            A[Average Case]
            A --> B[O(n log n)]
            A --> C[Worst Case O(n^2)]
            """
        },

        "breadth first search": {
            "beginner": """
            graph TD
            A[Start] --> B[Level 1]
            B --> C[Level 2]
            """,
            "intermediate": """
            graph TD
            A[Queue] --> B[Visit Neighbors]
            """,
            "advanced": """
            graph TD
            A[Unweighted Graph]
            A --> B[Shortest Path]
            """
        },

        "depth first search": {
            "beginner": """
            graph TD
            A[Start] --> B[Go Deep]
            B --> C[Backtrack]
            """,
            "intermediate": """
            graph TD
            A[Stack / Recursion]
            A --> B[Explore]
            """,
            "advanced": """
            graph TD
            A[DFS Tree]
            A --> B[Topological Sort]
            A --> C[SCC]
            """
        },

        "dijkstra": {
            "beginner": """
            graph TD
            A[Source] --> B[Closest Node]
            """,
            "intermediate": """
            graph TD
            A[Priority Queue]
            A --> B[Relax Edges]
            """,
            "advanced": """
            graph TD
            A[Greedy Choice]
            A --> B[No Negative Edges]
            """
        },

        "bellman ford": {
            "beginner": """
            graph TD
            A[Source] --> B[Relax All Edges]
            """,
            "intermediate": """
            graph TD
            A[V-1 Iterations]
            A --> B[Update Distances]
            """,
            "advanced": """
            graph TD
            A[Negative Cycle]
            A --> B[Detection]
            """
        },

        "greedy algorithm": {
            "beginner": """
            graph TD
            A[Choose Best Option]
            """,
            "intermediate": """
            graph TD
            A[Local Optimal]
            A --> B[Global Result]
            """,
            "advanced": """
            graph TD
            A[Greedy Proof]
            A --> B[Exchange Argument]
            """
        },

        "hashing": {
            "beginner": """
            graph TD
            A[Key] --> B[Hash Function]
            B --> C[Index]
            """,
            "intermediate": """
            graph TD
            A[Collision]
            A --> B[Chaining]
            A --> C[Open Addressing]
            """,
            "advanced": """
            graph TD
            A[Load Factor]
            A --> B[O(1) Average]
            """
        },

        "amortized analysis": {
            "beginner": """
            graph TD
            A[Operations] --> B[Average Cost]
            """,
            "intermediate": """
            graph TD
            A[Aggregate Method]
            A --> B[Accounting]
            """,
            "advanced": """
            graph TD
            A[Potential Method]
            A --> B[Energy Model]
            """
        },

        "segment tree": {
            "beginner": """
            graph TD
            A[Array] --> B[Segments]
            """,
            "intermediate": """
            graph TD
            A[Segment Tree]
            A --> B[Query]
            A --> C[Update]
            """,
            "advanced": """
            graph TD
            A[Range Query]
            A --> B[O(log n)]
            """
        },

        "red black tree": {
            "beginner": """
            graph TD
            A[Insert Node]
            A --> B[Recolor]
            """,
            "intermediate": """
            graph TD
            A[Rotate]
            A --> B[Balance]
            """,
            "advanced": """
            graph TD
            A[Height O(log n)]
            """
        },

        "topological sort": {
            "beginner": """
            graph TD
            A[Task] --> B[Dependency]
            """,
            "intermediate": """
            graph TD
            A[DAG]
            A --> B[Ordering]
            """,
            "advanced": """
            graph TD
            A[Build System]
            """
        },

        "network flow": {
            "beginner": """
            graph TD
            A[Source] --> B[Sink]
            """,
            "intermediate": """
            graph TD
            A[Residual Graph]
            A --> B[Augment Path]
            """,
            "advanced": """
            graph TD
            A[Max Flow Min Cut]
            """
        },

        "np completeness": {
            "beginner": """
            graph TD
            A[Problem]
            A --> B[Hard to Solve]
            """,
            "intermediate": """
            graph TD
            A[NP]
            A --> B[Polynomial Verification]
            """,
            "advanced": """
            graph TD
            A[Reduction]
            A --> B[NP-Complete]
            """
        }
    }

    return diagrams.get(topic, {}).get(level, "")
