"""
Problem 3: Number Analysis
Analyze a list of numbers provided by the user.
"""

def get_numbers_from_user():
    """
    Get numbers from user until they type 'done'.
    Return a list of numbers.

    Returns:
        list: List of numbers entered by user
    """
    numbers = []

    while True:
        user_input = input("Enter a number (or 'done' to finish): ").strip()
        if user_input.lower() == 'done':
            break
        try:
            # Accept integers or floats
            if '.' in user_input:
                num = float(user_input)
            else:
                num = int(user_input)
            numbers.append(num)
        except ValueError:
            print("Invalid number, please try again.")

    return numbers


def analyze_numbers(numbers):
    """
    Analyze the list and return a dictionary with:
    - count: number of elements
    - sum: sum of all numbers
    - average: average value
    - minimum: smallest number
    - maximum: largest number
    - even_count: count of even numbers
    - odd_count: count of odd numbers

    Args:
        numbers (list): List of numbers to analyze

    Returns:
        dict: Dictionary with analysis results, or None if list is empty
    """
    if not numbers:
        return None

    analysis = {}
    # Normalize numbers to floats for average/sum calculations
    nums = [float(x) for x in numbers]

    count = len(nums)
    total = sum(nums)
    average = total / count
    minimum = min(nums)
    maximum = max(nums)

    # For even/odd counting, consider integers only; treat x as even if it's integer-valued
    even_count = 0
    odd_count = 0
    for x in nums:
        if float(x).is_integer():
            if int(x) % 2 == 0:
                even_count += 1
            else:
                odd_count += 1

    analysis['count'] = count
    analysis['sum'] = total if not total.is_integer() else int(total)
    analysis['average'] = round(average, 2) if not average.is_integer() else float(int(average))
    # Keep min/max as int when they are integer-valued
    analysis['minimum'] = int(minimum) if float(minimum).is_integer() else minimum
    analysis['maximum'] = int(maximum) if float(maximum).is_integer() else maximum
    analysis['even_count'] = even_count
    analysis['odd_count'] = odd_count

    return analysis


def display_analysis(analysis):
    """
    Display the analysis in a formatted way.

    Args:
        analysis (dict): Dictionary containing analysis results
    """
    if not analysis:
        return

    print("\nAnalysis Results:")
    print("-" * 20)

    print(f"Count: {analysis.get('count')}")
    print(f"Sum: {analysis.get('sum')}")
    avg = analysis.get('average')
    if isinstance(avg, float):
        print(f"Average: {avg:.2f}")
    else:
        print(f"Average: {avg}")
    print(f"Minimum: {analysis.get('minimum')}")
    print(f"Maximum: {analysis.get('maximum')}")
    print(f"Even numbers: {analysis.get('even_count')}")
    print(f"Odd numbers: {analysis.get('odd_count')}")


def main():
    """Main function to run the number analyzer."""
    print("Number Analyzer")
    print("Enter numbers one at a time. Type 'done' when finished.")
    print()

    # Get numbers from user
    numbers = get_numbers_from_user()

    if not numbers:
        print("No numbers entered!")
        return

    # Analyze the numbers
    analysis = analyze_numbers(numbers)

    # Display the results
    display_analysis(analysis)


if __name__ == "__main__":
    main()