from test_generated_world import test_generate_world , test_emerge


# The order of weight values for each terrain type:
#WEIGHTS = [WEIGHT_OCEAN3, WEIGHT_OCEAN2, WEIGHT_OCEAN1, WEIGHT_BEACH, WEIGHT_GRASS, WEIGHT_MOUNTAIN, WEIGHT_SNOW]
WEIGHTS1 = [70, 10, 10, 10,10, 10, 10]      # Islands
WEIGHTS2 = [10, 30, 40, 10, 10, 10, 10]     #
WEIGHTS3 = [10, 15, 15, 15, 50, 15, 45]     # Lakes


test_generate_world(WEIGHTS1, random_seed = 21)
test_generate_world(WEIGHTS1, random_seed = 258)
test_generate_world(WEIGHTS2, random_seed = 7)
test_generate_world(WEIGHTS2, random_seed = 8)
test_generate_world(WEIGHTS3, random_seed = 16)
test_generate_world(WEIGHTS3, random_seed = 14)

"""
test_emerge(WEIGHTS1, random_seed = 21)
test_emerge(WEIGHTS1, random_seed = 7)
test_emerge(WEIGHTS1, random_seed = 16)
test_emerge(WEIGHTS1, random_seed = 28)
test_emerge(WEIGHTS1, random_seed = 8)
test_emerge(WEIGHTS1, random_seed = 14)
"""