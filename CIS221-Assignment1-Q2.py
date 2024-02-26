class Chocolate:
    def __init__(self, weight, price, type):
        # Initialize a Chocolate object with weight, price, and type attributes
        self.weight = weight
        self.price = price
        self.type = type

    def __str__(self):
        # String representation of Chocolate object
        return f"Chocolate(type='{self.type}', weight={self.weight}, price={self.price})"

def compare_chocolates(chocolate):
    # Comparison function for sorting chocolates by price
    return chocolate.price

def merge_sort(arr):
    """Merge sort algorithm to sort chocolates based on price."""
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return merge(left_half, right_half)

def merge(left, right):
    """Merge two sorted lists into a single sorted list."""
    merged = []
    left_index = right_index = 0

    while left_index < len(left) and right_index < len(right):
        if compare_chocolates(left[left_index]) < compare_chocolates(right[right_index]):
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return merged

def distribute_chocolates_iterative(chocolates, students):
    """Distribute chocolates to students iteratively."""
    # Sort chocolates based on price using merge sort
    chocolates_sorted = merge_sort(chocolates)

    # Create an empty dictionary to store distribution of chocolates to students
    distribution = {}

    # Iterate over each student and assign them a chocolate
    for i in range(len(students)):
        distribution[students[i]] = chocolates_sorted[i]

    return distribution

def distribute_chocolates_recursive(chocolates, students):
    """Distribute chocolates to students recursively."""
    # Base case: if no chocolates or no students, return empty distribution
    if not chocolates or not students:
        return {}

    # Sort chocolates based on price using merge sort
    chocolates_sorted = merge_sort(chocolates)

    # Create an empty dictionary to store distribution of chocolates to students
    distribution = {}

    # Assign the first chocolate to the first student
    distribution[students[0]] = chocolates_sorted[0]

    # Recursively distribute remaining chocolates to remaining students
    remaining_distribution = distribute_chocolates_recursive(chocolates_sorted[1:], students[1:])

    # Merge the remaining distribution with the current distribution
    distribution.update(remaining_distribution)

    return distribution

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
chocolates = [Chocolate(10, 5, 'dark'), Chocolate(15, 7, 'milk'), Chocolate(8, 3, 'white'), Chocolate(12, 6, 'coconut'), Chocolate(18, 8, 'caramel'), Chocolate(9, 4, 'hazelnut')]
students = ['Shouq', 'Alya', 'Abdullah', 'Sarah', 'Ali']

# Iterative distribution
distribution_iterative = distribute_chocolates_iterative(chocolates, students)
print("Iterative distribution:")
for student, chocolate in distribution_iterative.items(): # to make the output clearer. it was not clear before.
    print(f"{student}: {chocolate}")

# Recursive distribution
distribution_recursive = distribute_chocolates_recursive(chocolates, students)
print("\nRecursive distribution:")
for student, chocolate in distribution_recursive.items(): # to make the output clearer. it was not clear before.
    print(f"{student}: {chocolate}")

# Test Cases for sorting chocolates
print("\nSorted Chocolates by Weight:")
for chocolate in sort_chocolates_by_weight(chocolates):
    print(chocolate)

print("\nSorted Chocolates by Price:")
for chocolate in sort_chocolates_by_price(chocolates):
    print(chocolate)