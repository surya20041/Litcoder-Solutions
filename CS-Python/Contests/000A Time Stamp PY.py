class TimeTravelersArchive:
    def __init__(self):
        # Initialize an empty dictionary to store data with keys as identifiers
        # Each key corresponds to a list of timestamped values
        self.archive = {}

    def store(self, key, value, timestamp):
        # Check if the key already exists in the archive
        if key not in self.archive:
            # If not, create an empty list for the key
            self.archive[key] = []

        # Append the new value along with its timestamp to the list for the given key
        self.archive[key].append((timestamp, value))

    def retrieve(self, key, timestamp):
        # Check if the key exists in the archive
        if key not in self.archive:
            return 

        # Get the list of timestamped values for the given key
        values = self.archive[key]

        # Perform binary search to find the closest timestamp to the given timestamp
        index = self.binary_search(values, timestamp)

        # Check if a matching timestamp was found
        if index == -1:
            return "empty"
        else:
            # Return the corresponding value for the found timestamp
            return values[index][1]

    def binary_search(self, values, timestamp):
        # Implement binary search to find the closest timestamp in the sorted list
        left, right = 0, len(values) - 1
        result = -1

        while left <= right:
            mid = left + (right - left) // 2

            if values[mid][0] == timestamp:
                return mid
            elif values[mid][0] < timestamp:
                result = mid
                left = mid + 1
            else:
                right = mid - 1

        return result


def process_commands():
    # Create an instance of the TimeTravelersArchive class
    archive = TimeTravelersArchive()
    # Store the results of retrieve operations for later printing
    results = []

    while True:
        try:
            # Get user input for commands
            command = input()
        except EOFError:
            # Break the loop if the end of the input is reached
            break

        if command.lower() == 'exit':
            # Break the loop if the user enters 'exit'
            break

        # Split the command into parts
        parts = command.split()
        operation = parts[0].lower()

        # Check the operation and execute the corresponding method
        if operation == "store" and len(parts) == 4:
            archive.store(parts[1], parts[2], int(parts[3]))
        elif operation == "retrieve" and len(parts) == 3:
            # Perform retrieve operation and store the result for later printing
            result = archive.retrieve(parts[1], int(parts[2]))
            results.append(result)
        else:
            # Handle invalid commands or print a message for unsupported operations
            print()

    # Return the list of results from retrieve operations
    return results


if __name__ == "__main__":
    # Process user commands and store the results
    results = process_commands()
    # Print the results of retrieve operations
    for result in results:
        print(result)
