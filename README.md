# company-lunch
This was a project created as part of a CCAI-311 (Optimization and Regression )

# Describe of the problem
A company is making lunch for a business meeting.
It will serve chicken sandwiches, light chicken sandwiches, and vegetarian sandwiches.
A chicken sandwich has 1 serving of vegetables, 4 slices of chicken, 1 slice of cheese, and 2 slices of bread. The price of each sandwich is 10 SR. A light chicken sandwich has 2 servings of vegetables, 2 slices of chicken, 1 slice of cheese, and 3 slices of bread, the price of each sandwich is 15 SR. A vegetarian sandwich has 3 servings of vegetables, 4 slices of cheese, and 3 slices of bread. The price of each sandwich is 20 SR.

In total, the company has available 5 bags of chicken, each of which has 80 slices of chicken, 10 loaves of bread, each with 30 slices, 200 servings of vegetables, and 9 bags of cheese, each with 100 slices of cheese.
How many of each sandwich can be produced if the goal is to maximize the benefit of sandwiches?
 
The goal is to maximize the benefit.

### We wish to maximize the number of sandwiches, so let:
X= chicken sandwich

Y= light chicken sandwich

Z= vegetarian sandwich

### The total price and cost of sandwiches are given by:
benefit = price - cost

### The constraints
chicken sandwich, light chicken sandwich the required number of chicken

4X+2Y<=400

chicken sandwich, light chicken sandwich, vegetarian sandwich the required number of bread

2X+3Y+3Z<=300

chicken sandwich, light chicken sandwich, and vegetarian sandwich, with the required number of vegetables.

X+2Y+3Z<=200

chicken sandwich, light chicken sandwich, and vegetarian sandwich, with the required number of slices of cheese.

X+Y+4Z<= 900

# metaheuristics
### We used two metaheuristics to solve this problem:
1-BASIC LOCAL SEARCH

2-TABU SEARCH

