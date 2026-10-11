from collections import defaultdict
import heapq

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj = defaultdict(list)
        for i, [a, b] in enumerate(edges):
            adj[a].append((b, succProb[i]))
            adj[b].append((a, succProb[i]))

        # modified dijkstra's algo
        # probabilities list initialized with 0s
        probabilities = [0] * n
        
        # max heap initialized with (1, start_node) => same as min heap with neg values
        max_heap = [(-1, start_node)]

        # while heap:
        while max_heap:
            # pop cur_prob, cur_node
            neg_prob, node = heapq.heappop(max_heap)
            prob = -neg_prob

            # if cur_prob < probabilities[cur_node] => continue
            if prob < probabilities[node]:
                continue

            # if cur_node == end_node: return cur_prob
            if node == end_node:
                return prob

            # for all neighbors of cur_node
            for neighbor, weight in adj[node]:
                # if probabilities[neighbor] < cur_prob * edge weight:
                if probabilities[neighbor] < prob * weight:
                    # add node to heap
                    heapq.heappush(max_heap, (-(prob * weight), neighbor))
                    # update probabilities
                    probabilities[neighbor] = prob * weight
            
        # return 0 if couldn't reach end node
        return 0