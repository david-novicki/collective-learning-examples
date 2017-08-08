import algorithms
from recommendations import critics
  
print algorithms.sim_distance(critics, 'Lisa Rose', 'Michael Phillips')
print algorithms.sim_pearson(critics, 'Lisa Rose', 'Michael Phillips')
print algorithms.topMatches(critics, 'Lisa Rose')