import random 
import sets
import numpy

# Expected number of steps for all possible outcomes to happen at least once. 
# Dividing by number of reporters to allow for more than one outcome per step.
def expected_steps_per_period(n, r):
    return sum([float(n)/k for k in range(1, n+1)]) / r
        
def covers_all_positive_ints(ints, max):
  for i in range(1, max+1):
      if i not in ints:
          return False
  return True

def calculate_coverage_time(reporters):
    run_history = []
    for run in range(0, EXPERIMENTAL_RUNS):
        coverage_set = sets.Set()
        steps = 0
        # as long as not all values are present, keep adding random integers
        while not covers_all_positive_ints(coverage_set, RANGE_UPPER): 
            [coverage_set.add(random.randint(1, RANGE_UPPER)) 
              for r in range(0, reporters)]
            steps += 1
        run_history.append(steps)
    return numpy.mean(run_history), expected_steps_per_period(RANGE_UPPER, reporters);

RANGE_UPPER = 999
EXPERIMENTAL_RUNS = 10
experiments_stats = []

for reporter_count in [1, 2, 5, 10, 20, 50, 100, 500, 1000, 2000, 5000]:
    avg_sim_steps, expected_steps = calculate_coverage_time(reporter_count)
    experiments_stats.append([reporter_count, avg_sim_steps, expected_steps])
    
print(experiments_stats)
