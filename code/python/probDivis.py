def count_divisible(w, pos, current_state, n):
    # Base case: if we reach the end of the string, check if divisible
    if pos == len(w):
        return 1 if current_state == 0 else 0

    # If the current character is '_', try all digits 0-9 with equal probability
    if w[pos] == '_':
        probability_sum = 0
        for digit in range(10):
            new_state = (10 * current_state + digit) % n
            probability_sum += count_divisible(w, pos + 1, new_state, n) / 10
        return probability_sum
    else:
        # If the current character is a specific digit, proceed with the corresponding transition
        new_digit = int(w[pos])
        new_state = (10 * current_state + new_digit) % n
        return count_divisible(w, pos + 1, new_state, n)

def probability_divisible_by_n(w, n):
    return count_divisible(w, 0, 0, n)

# Example usage
w = "1_3"
n = 7
result = probability_divisible_by_n(w, n)
print(f"The probability that {w} is divisible by {n} is {result:.3f}")