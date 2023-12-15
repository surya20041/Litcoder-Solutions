class QueueUsingTwoStacks:
    def __init__(self):
        # Initialize two stacks, one for enqueue and one for dequeue
        self.stack_enqueue = []
        self.stack_dequeue = []

    def enqueue(self, x):
        # To enqueue, simply push the element onto stack_enqueue
        self.stack_enqueue.append(x)

    def dequeue(self):
        # Check if both stacks are empty
        if not self.stack_enqueue and not self.stack_dequeue:
            return None

        # If stack_dequeue is empty, transfer elements from stack_enqueue
        if not self.stack_dequeue:
            while self.stack_enqueue:
                self.stack_dequeue.append(self.stack_enqueue.pop())

        # Pop the element from stack_dequeue (which contains elements in the correct order)
        return self.stack_dequeue.pop()

    def get_front(self):
        # Check if both stacks are empty
        if not self.stack_enqueue and not self.stack_dequeue:
            return None

        # If stack_dequeue is empty, transfer elements from stack_enqueue
        if not self.stack_dequeue:
            while self.stack_enqueue:
                self.stack_dequeue.append(self.stack_enqueue.pop())

        # Return the element at the front without removing it
        return self.stack_dequeue[-1]


# Function to process the input queries
def doSomething(queries):
    # Create an instance of the QueueUsingTwoStacks class
    queue = QueueUsingTwoStacks()
    # Initialize a list to store the results
    results = []

    for query in queries:
        # Check the type of query and perform the corresponding operation
        if query[0] == 1:
            # Enqueue operation
            queue.enqueue(query[1])
        elif query[0] == 2:
            # Dequeue operation
            queue.dequeue()
        elif query[0] == 3:
            # Get front element operation
            front_element = queue.get_front()
            if front_element is not None:
                # Append the result to the list
                results.append(front_element)

    # Return the list of results
    return results


# Function to take user input for queries
def get_user_input():
    # Read user input as a comma-separated string of queries
    input_str = input()
    # Initialize an empty list to store the queries
    queries = []

    # Iterate through the comma-separated string and parse each query
    for query_str in input_str.split(","):
        query_parts = query_str.split()
        query_type = int(query_parts[0])

        if query_type == 1:
            # Enqueue operation: Append a tuple with query type and element to the list
            element = int(query_parts[1])
            queries.append((1, element))
        elif query_type == 2:
            # Dequeue operation: Append a tuple with only the query type to the list
            queries.append((2,))
        elif query_type == 3:
            # Get front element operation: Append a tuple with only the query type to the list
            queries.append((3,))

    # Return the list of parsed queries
    return queries


# Example usage with user input:
user_queries = get_user_input()
output = doSomething(user_queries)

# Print the results
for result in output:
    if result is not None:
        print(result)
