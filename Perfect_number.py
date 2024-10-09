def is_perfect_number(n):
    if n < 1:
        return False

    # Calculate the sum of proper divisors
    divisors_sum = sum(i for i in range(1, n) if n % i == 0)
    
    # Check if the sum of divisors equals the original number
    return divisors_sum == n

# Example usage
num = 6
if is_perfect_number(num):
    print(f"{num} is a perfect number")
else:
    print(f"{num} is not a perfect number")
