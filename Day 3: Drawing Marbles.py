# Number of red and blue marbles in the bag
red_marbles = 3
blue_marbles = 4

# Probability of drawing a red marble first
probability_red_first = red_marbles / (red_marbles + blue_marbles)

# Probability of drawing a blue marble second, given that the first marble was red
probability_blue_second_given_red_first = blue_marbles / (red_marbles + blue_marbles - 1)

# Calculate the conditional probability
conditional_probability = probability_red_first * probability_blue_second_given_red_first

print("The probability that the second marble is blue, given that the first marble is red, is:", conditional_probability)
