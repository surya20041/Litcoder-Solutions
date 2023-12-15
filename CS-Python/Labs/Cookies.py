import heapq

def combine_candies_to_target(target, candies):
    heapq.heapify(candies)  # Convert the list of candies to a min heap

    steps = 0
    while candies[0] < target:
        # Take the two least sweet candies
        least_sweet = heapq.heappop(candies)
        second_least_sweet = heapq.heappop(candies)

        # Calculate the sweetness of the combined candy
        combined_sweetness = least_sweet + 2 * second_least_sweet

        # Put the combined candy back into the heap
        heapq.heappush(candies, combined_sweetness)

        steps += 1

    return steps

# Input from user for Exercise-1
target_input1 = int(input())
candies_input1 = list(map(int, input().split()))

result1 = combine_candies_to_target(target_input1, candies_input1)
print(result1)

