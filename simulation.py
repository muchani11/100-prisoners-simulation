import argparse
import random
from collections import deque
import timeit

STARTING_SIMS = 100000
PRISONER_POPULATION = 100

def initialize_parser():
    parser = argparse.ArgumentParser(description='Retrieves number of simulations')
    parser.add_argument('--simulations', type=int, help='Number of simulations to run (default is 100,000)')
    parser.add_argument('--population', type=int, help='Size of initial prisoner population (default is 100)')
    return parser


def populate_number_loops(k):
    initial_nums = random.sample(range(1, k+1), k)
    visited = set()
    for num in initial_nums:
        if num not in visited:
            new_loop_size = 0
            visited.add(num)

            queue = deque()
            queue.append(num)
            while queue:
                next_pointer = queue.popleft()
                new_loop_size += 1
                next_number = initial_nums[next_pointer-1]
                if next_number not in visited:
                    queue.append(next_number)
                    visited.add(next_number)
            if new_loop_size > (k / 2):
                return False
    
    return True


parser = initialize_parser()
args = parser.parse_args()
simulations = args.simulations if args.simulations else STARTING_SIMS
population = args.population if args.population else PRISONER_POPULATION
count_successes = 0.0
start = timeit.default_timer()

for i in range(simulations):
    no_loop_too_large = populate_number_loops(population)
    if no_loop_too_large:
        count_successes += 1

end = timeit.default_timer()

print("Results: {} out of {} simulations successful for {} prisoners".format(int(count_successes), simulations, population))
print("Success rate: {}%".format(100 * count_successes / simulations))
print("Time taken: {} sec".format(round(end - start, 3)))