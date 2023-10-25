# Total number of possible outcomes when rolling two dice
total_outcomes = 6 * 6  # Each die has 6 sides

# Number of successful outcomes (different values and sum is 6)
successful_outcomes = 0
for die1 in range(1, 7):
    for die2 in range(1, 7):
        if die1 != die2 and die1 + die2 == 6:
            successful_outcomes += 1

# Calculate the probability
probability = successful_outcomes / total_outcomes

print(f"The probability that the values are different and the sum is 6 is {probability:.2f}")
