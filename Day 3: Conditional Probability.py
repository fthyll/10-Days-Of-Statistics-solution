# Probability that both children are boys given that one of them is a boy

# Total possibilities (BB, BG, GB, GG)
total_possibilities = 4

# Possibilities where at least one is a boy (BB, BG, GB)
at_least_one_boy = 3

# Possibilities where both are boys (BB)
both_boys = 1

# Calculate the conditional probability
conditional_probability = both_boys / at_least_one_boy

print("The probability that both children are boys, given that one of them is a boy, is:", conditional_probability)
