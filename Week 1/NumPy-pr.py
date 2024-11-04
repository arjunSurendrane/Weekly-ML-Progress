import numpy as np

score = np.array([4,5,3,3,5,3,2])
print(score)

print("sum", np.sum(score))
print("average", np.average(score))
print("mean", np.mean(score))


# 2D array
scores_round1 = [8, 10, 12, 15]
scores_round2 = [9, 11, 14, 16]
scores = np.array([scores_round1, scores_round2])
print(scores)

# Question 5: Finding the Highest Score in Each Round
# Q: Now that you have scores in two rounds, what if you want to find the highest score in each round?

highest_score = np.max(scores, axis=1)
#  axis =1 means - look at each row separately.
print(highest_score)

# Multiplying Each Score by 2

multiplied_score = scores *2
print(multiplied_score)