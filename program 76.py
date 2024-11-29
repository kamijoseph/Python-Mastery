
import random 
# Simulating a Bernoulli trial
def bernoulli_trial(p):
    return 1 if random.random() < p else 0

# Simulating 10 trials with success probability 0.7
trials = [bernoulli_trial(0.7) for _ in range(10)]
print("Bernoulli Trials:", trials)
