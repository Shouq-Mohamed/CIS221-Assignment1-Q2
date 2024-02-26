class Chocolate:
    def __init__(self, weight, price, type):
        # Initialize a Chocolate object with weight, price, and type attributes
        self.weight = weight  # Set the weight attribute
        self.price = price    # Set the price attribute
        self.type = type      # Set the type attribute

    def __str__(self):
        # String representation of Chocolate object
        return f"Chocolate(type='{self.type}', weight={self.weight}, price={self.price})"

def compare_chocolates(chocolate):
    # Comparison function for sorting chocolates by price
    return chocolate.price  # Return the price of a chocolate for comparison

def merge_sort(arr):
    """Merge sort algorithm to sort chocolates based on price."""
    if len(arr) <= 1:  # if the array has 0 or 1 element, it's already sorted
        return arr

    mid = len(arr) // 2  # Calculate the middle index
    left_half = merge_sort(arr[:mid])  # Recursively sort the left half of the array
    right_half = merge_sort(arr[mid:])  # Recursively sort the right half of the array

    return merge(left_half, right_half)  # Merge the sorted halves

def merge(left, right):
    """Merge two sorted lists into a single sorted list."""
    merged = []  # Initialize an empty list to store merged elements
    left_index = right_index = 0  # Initialize indices for left and right lists

    while left_index < len(left) and right_index < len(right):
        # Merge elements from left and right lists in sorted order
        if compare_chocolates(left[left_index]) < compare_chocolates(right[right_index]):
            merged.append(left[left_index])  # Append element from left list
            left_index += 1  # Move to the next element in the left list
        else:
            merged.append(right[right_index])  # Append element from right list
            right_index += 1  # Move to the next element in the right list

    merged.extend(left[left_index:])  # Add remaining elements from left list
    merged.extend(right[right_index:])  # Add remaining elements from right list

    return merged  # Return the merged list

def distribute_chocolates_iterative(chocolates, students):
    """Distribute chocolates to students iteratively."""
    chocolates_sorted = merge_sort(chocolates)  # Sort chocolates based on price using merge sort
    distribution = {}  # Initialize an empty dictionary for distribution

    # Iterate over each student and assign them a chocolate
    for i in range(len(students)):
        distribution[students[i]] = chocolates_sorted[i]

    return distribution  # Return the distribution dictionary

def distribute_chocolates_recursive(chocolates, students):
    """Distribute chocolates to students recursively."""
    if not chocolates or not students:  # if no chocolates or no students, return empty distribution
        return {}

    chocolates_sorted = merge_sort(chocolates)  # Sort chocolates based on price using merge sort
    distribution = {}  # Initialize an empty dictionary for distribution

    distribution[students[0]] = chocolates_sorted[0]  # Assign the first chocolate to the first student

    # Recursively distribute remaining chocolates to remaining students
    remaining_distribution = distribute_chocolates_recursive(chocolates_sorted[1:], students[1:])

    # Merge the remaining distribution with the current distribution
    distribution.update(remaining_distribution)

    return distribution  # Return the distribution dictionary

# Sorting chocolates by weight and price after distribution
def sort_chocolates_by_weight(chocolates):
    def get_weight(chocolate):
        return chocolate.weight
    return sorted(chocolates, key=get_weight)

def sort_chocolates_by_price(chocolates):
    def get_price(chocolate):
        return chocolate.price
    return sorted(chocolates, key=get_price)

# Test cases
chocolates = [Chocolate(10, 5, 'dark'), Chocolate(15, 7, 'milk'), Chocolate(8, 3, 'white'), Chocolate(12, 6, 'coconut'), Chocolate(18, 8, 'caramel'), Chocolate(9, 4, 'hazelnut'), Chocolate(20, 10, 'white'), Chocolate(7, 2, 'dark'), Chocolate(14, 5, 'milk'), Chocolate(11, 7, 'coconut')]
students = ['Shouq', 'Alya', 'Abdullah', 'Sarah', 'Ali']

# Iterative distribution
distribution_iterative = distribute_chocolates_iterative(chocolates, students)
print("Iterative distribution:")
for student, chocolate in distribution_iterative.items():  # Print the distribution
    print(f"{student}: {chocolate}")

# Recursive distribution
distribution_recursive = distribute_chocolates_recursive(chocolates, students)
print("\nRecursive distribution:")
for student, chocolate in distribution_recursive.items():  # Print the distribution
    print(f"{student}: {chocolate}")

# Test Cases for sorting chocolates
print("\nSorted Chocolates by Weight:")
for chocolate in sort_chocolates_by_weight(chocolates):  # Print chocolates sorted by weight
    print(chocolate)

print("\nSorted Chocolates by Price:")
for chocolate in sort_chocolates_by_price(chocolates):  # Print chocolates sorted by price
    print(chocolate)
