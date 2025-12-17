knowledge_base = {

    "dynamic programming": {
        "beginner": {
            "definition": "Dynamic Programming solves problems by remembering previously computed results.",
            "steps": [
                "Break the problem into smaller parts",
                "Solve each part once",
                "Reuse stored results"
            ],
            "analogy": "Like remembering solved exam questions.",
            "engineering_example": "Simple optimization problems."
        },
        "intermediate": {
            "definition": "Dynamic Programming handles overlapping subproblems using memoization or tabulation.",
            "steps": [
                "Identify overlapping subproblems",
                "Define states and transitions",
                "Use DP table"
            ],
            "analogy": "Using notes while solving math problems.",
            "engineering_example": "Knapsack, LCS."
        },
        "advanced": {
            "definition": "DP is an algorithmic paradigm exploiting optimal substructure and overlapping subproblems.",
            "steps": [
                "Formulate recurrence",
                "Analyze complexity",
                "Optimize space"
            ],
            "analogy": "Caching database query results.",
            "engineering_example": "Compiler optimization, AI planning."
        }
    },

    "divide and conquer": {
        "beginner": {
            "definition": "Divide and Conquer breaks a problem into smaller parts.",
            "steps": ["Divide", "Solve", "Combine"],
            "analogy": "Cutting a pizza into slices.",
            "engineering_example": "Sorting problems."
        },
        "intermediate": {
            "definition": "Divide and Conquer solves independent subproblems recursively.",
            "steps": ["Split problem", "Recursive solve", "Merge"],
            "analogy": "Splitting office work among teams.",
            "engineering_example": "Merge sort, Binary search."
        },
        "advanced": {
            "definition": "Divide and Conquer efficiency is analyzed using recurrence relations.",
            "steps": ["Form recurrence", "Apply Master theorem"],
            "analogy": "Hierarchical company management.",
            "engineering_example": "FFT, Strassen algorithm."
        }
    },

    "binary search": {
        "beginner": {
            "definition": "Binary Search finds an element by repeatedly dividing a sorted list.",
            "steps": ["Check middle", "Discard half"],
            "analogy": "Finding a word in a dictionary.",
            "engineering_example": "Searching sorted lists."
        },
        "intermediate": {
            "definition": "Binary Search reduces search space logarithmically.",
            "steps": ["Mid calculation", "Comparison", "Repeat"],
            "analogy": "Guessing a number game.",
            "engineering_example": "Database indexing."
        },
        "advanced": {
            "definition": "Binary Search is a logarithmic-time algorithm used in decision problems.",
            "steps": ["Invariant maintenance", "Boundary analysis"],
            "analogy": "Optimized decision making.",
            "engineering_example": "Optimization problems."
        }
    },

    "merge sort": {
        "beginner": {
            "definition": "Merge Sort sorts by dividing and merging lists.",
            "steps": ["Divide", "Merge"],
            "analogy": "Sorting two piles of cards.",
            "engineering_example": "Basic sorting."
        },
        "intermediate": {
            "definition": "Merge Sort is a stable divide-and-conquer sorting algorithm.",
            "steps": ["Split array", "Merge sorted halves"],
            "analogy": "Combining sorted exam papers.",
            "engineering_example": "External sorting."
        },
        "advanced": {
            "definition": "Merge Sort guarantees O(n log n) time complexity.",
            "steps": ["Recurrence analysis"],
            "analogy": "Balanced task distribution.",
            "engineering_example": "Large-scale data processing."
        }
    },

    "quick sort": {
        "beginner": {
            "definition": "Quick Sort sorts elements around a pivot.",
            "steps": ["Choose pivot", "Partition"],
            "analogy": "Organizing people by height.",
            "engineering_example": "Fast sorting."
        },
        "intermediate": {
            "definition": "Quick Sort partitions arrays recursively.",
            "steps": ["Pivot selection", "Recursive sort"],
            "analogy": "Grouping objects.",
            "engineering_example": "System-level sorting."
        },
        "advanced": {
            "definition": "Quick Sort has average O(n log n) but worst O(n²).",
            "steps": ["Partition analysis"],
            "analogy": "Risk-based decisions.",
            "engineering_example": "Competitive programming."
        }
    },

    "breadth first search": {
        "beginner": {
            "definition": "BFS explores nodes level by level.",
            "steps": ["Visit neighbors"],
            "analogy": "Water spreading evenly.",
            "engineering_example": "Shortest path."
        },
        "intermediate": {
            "definition": "BFS uses a queue to traverse graphs.",
            "steps": ["Queue processing"],
            "analogy": "Ripple effect.",
            "engineering_example": "Network routing."
        },
        "advanced": {
            "definition": "BFS guarantees shortest paths in unweighted graphs.",
            "steps": ["Graph traversal"],
            "analogy": "Layered exploration.",
            "engineering_example": "Broadcast systems."
        }
    },

    "depth first search": {
        "beginner": {
            "definition": "DFS explores deeply before backtracking.",
            "steps": ["Go deep", "Backtrack"],
            "analogy": "Exploring a maze.",
            "engineering_example": "Path finding."
        },
        "intermediate": {
            "definition": "DFS uses recursion or stack.",
            "steps": ["Recursive calls"],
            "analogy": "Going down a tunnel.",
            "engineering_example": "Cycle detection."
        },
        "advanced": {
            "definition": "DFS enables topological sorting and SCC detection.",
            "steps": ["Timestamping"],
            "analogy": "Depth exploration.",
            "engineering_example": "Compiler design."
        }
    },

    "dijkstra": {
        "beginner": {
            "definition": "Dijkstra finds shortest paths.",
            "steps": ["Pick nearest node"],
            "analogy": "Finding cheapest route.",
            "engineering_example": "GPS navigation."
        },
        "intermediate": {
            "definition": "Dijkstra relaxes edges using priority queues.",
            "steps": ["Edge relaxation"],
            "analogy": "Cost optimization.",
            "engineering_example": "Routing protocols."
        },
        "advanced": {
            "definition": "Dijkstra fails with negative edges.",
            "steps": ["Greedy analysis"],
            "analogy": "Local optimization.",
            "engineering_example": "Network design."
        }
    },

    "bellman ford": {
        "beginner": {
            "definition": "Bellman-Ford finds shortest paths with negative weights.",
            "steps": ["Relax edges repeatedly"],
            "analogy": "Double checking routes.",
            "engineering_example": "Financial modeling."
        },
        "intermediate": {
            "definition": "Bellman-Ford detects negative cycles.",
            "steps": ["V-1 iterations"],
            "analogy": "Repeated verification.",
            "engineering_example": "Distributed systems."
        },
        "advanced": {
            "definition": "Bellman-Ford runs in O(VE) time.",
            "steps": ["Complexity analysis"],
            "analogy": "Thorough auditing.",
            "engineering_example": "Network protocols."
        }
    },

    "greedy algorithm": {
        "beginner": {
            "definition": "Greedy chooses the best local option.",
            "steps": ["Pick best choice"],
            "analogy": "Choosing biggest candy.",
            "engineering_example": "Simple scheduling."
        },
        "intermediate": {
            "definition": "Greedy may not always give optimal solutions.",
            "steps": ["Proof required"],
            "analogy": "Short-term decisions.",
            "engineering_example": "Huffman coding."
        },
        "advanced": {
            "definition": "Greedy correctness depends on matroid structure.",
            "steps": ["Exchange argument"],
            "analogy": "Structured choices.",
            "engineering_example": "Optimization theory."
        }
    },

    "hashing": {
        "beginner": {
            "definition": "Hashing stores data for fast access.",
            "steps": ["Compute hash"],
            "analogy": "Library indexing.",
            "engineering_example": "Dictionaries."
        },
        "intermediate": {
            "definition": "Hashing handles collisions.",
            "steps": ["Collision resolution"],
            "analogy": "Shared lockers.",
            "engineering_example": "Databases."
        },
        "advanced": {
            "definition": "Hashing enables O(1) average access.",
            "steps": ["Load factor analysis"],
            "analogy": "Perfect filing.",
            "engineering_example": "Cryptography."
        }
    },

    "amortized analysis": {
        "beginner": {
            "definition": "Amortized analysis averages cost over operations.",
            "steps": ["Average cost"],
            "analogy": "Monthly savings.",
            "engineering_example": "Dynamic arrays."
        },
        "intermediate": {
            "definition": "Amortized analysis explains expensive operations.",
            "steps": ["Aggregate method"],
            "analogy": "Long-term budgeting.",
            "engineering_example": "Stack operations."
        },
        "advanced": {
            "definition": "Amortized analysis uses accounting and potential methods.",
            "steps": ["Potential function"],
            "analogy": "Energy storage.",
            "engineering_example": "Advanced data structures."
        }
    }
}
