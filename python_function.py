def largest_number(num1: int, num2: int) -> int:
    """
    This function returns the largest
    number of two numbers
    """

    if isinstance(num1, int) and isinstance(num2, int):
        if num1 > num2:
            return(f"Number {num1} is larger then number {num2}")
        else:
            return (f"Number {num2} is larger then number {num1}")
    else:
        return "Please enter the numbers"

print(largest_number(3, 2))