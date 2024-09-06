Problem Description
Set A contains m points (x, y coordinates).
Set B contains n points (x, y coordinates).
The goal is to find pairs of points (one from Set A and the other from Set B) such that the Euclidean distance between the two points is less than a given threshold ε.
Problem 1: Brute Force Solution
In this problem, a brute-force approach is used to compare every point in Set A with every point in Set B and calculate the Euclidean distance. If the distance is less than ε, the pair is returned.

Problem 2: Optimized Solution with KD-Tree
In this problem, an optimized approach using a KD-Tree is implemented. This approach significantly reduces the complexity of finding pairs by organizing the points from Set B into a KD-Tree. It efficiently queries points that are within a radius ε from each point in Set A, reducing the number of distance calculations required.

Setup Instructions
Install Required Libraries:

You need to have Python installed. Additionally, you need the following Python libraries:

```
pip install scipy
pip install colorama

```
Clone the Repository:

Clone this repository to your local machine.

```
git clone git@github.com:zaid-ali753/ai-based-sol.git
cd AI-BASED-SOL

```
Running the Code:

There are two Python files:

solution_one.py: The brute force solution for small values of m and n.
solution_two.py: The optimized solution using KD-Tree for larger values of m and n.
Run either of these using the following command:

```
python solution_one.py

```

or

```

python solution_two.py

```

Example Output

For both solution_one.py and solution_two.py, the program will generate random sets of points and output pairs of points (A, B) where the distance between A and B is less than the specified ε.

How I Used GPT and Studied KD-Tree

For Problem 2, I sought a more efficient approach to handle large values of m and n. Using GPT, I explored KDTree optimization techniques, and it suggested using a KD-Tree for faster spatial queries. I researched how KD-Trees work and learned that they help reduce the complexity of finding nearest neighbors in multidimensional space. By constructing a KD-Tree for Set B, I was able to efficiently query points within a given radius from points in Set A, which improved the solution's performance.