"""
Problem 2: Temperature Converter
Convert between Celsius and Fahrenheit temperatures.
"""

def celsius_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit.
    Formula: F = (C × 9/5) + 32

    Args:
        celsius (float): Temperature in Celsius

    Returns:
        float: Temperature in Fahrenheit
    """
    try:
        c = float(celsius)
    except (TypeError, ValueError):
        raise TypeError("celsius must be a number")

    return (c * 9.0 / 5.0) + 32.0


def fahrenheit_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius.
    Formula: C = (F - 32) × 5/9

    Args:
        fahrenheit (float): Temperature in Fahrenheit

    Returns:
        float: Temperature in Celsius
    """
    try:
        f = float(fahrenheit)
    except (TypeError, ValueError):
        raise TypeError("fahrenheit must be a number")

    return (f - 32.0) * 5.0 / 9.0


def temperature_converter():
    """
    Interactive temperature converter.
    Ask user for:
    1. Temperature value
    2. Current unit (C or F)
    3. Convert and display result
    """
    print("Temperature Converter")
    print("-" * 30)

    # Get temperature value
    while True:
        val = input("Enter temperature value: ").strip()
        try:
            temp = float(val)
            break
        except ValueError:
            print("Please enter a valid number for temperature.")

    # Get unit
    while True:
        unit = input("Enter unit (C or F): ").strip().upper()
        if unit in ("C", "F"):
            break
        print("Please enter 'C' for Celsius or 'F' for Fahrenheit.")

    if unit == "C":
        converted = celsius_to_fahrenheit(temp)
        print(f"{temp:.2f}°C is {converted:.2f}°F")
    else:
        converted = fahrenheit_to_celsius(temp)
        print(f"{temp:.2f}°F is {converted:.2f}°C")


# Test cases (DO NOT MODIFY)
if __name__ == "__main__":
    # Test conversions
    print("Running tests...")

    # Test Celsius to Fahrenheit
    assert celsius_to_fahrenheit(0) == 32, "0°C should be 32°F"
    assert celsius_to_fahrenheit(100) == 212, "100°C should be 212°F"

    # Test Fahrenheit to Celsius
    assert fahrenheit_to_celsius(32) == 0, "32°F should be 0°C"
    assert fahrenheit_to_celsius(212) == 100, "212°F should be 100°C"

    print("All tests passed!")
    print()

    # Run interactive converter
    temperature_converter()