import random
import math
from scipy.spatial import KDTree
from colorama import Fore, Style

def generate_random_cord(num_points, lower_bound=-100, upper_bound=100):
    """Code to generate list of coordinates"""
    return [(random.uniform(lower_bound, upper_bound), random.uniform(lower_bound, upper_bound)) for _ in range(num_points)]

def euclidean_distance(point1, point2):
    """Calculate the Euclidean distance"""
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def find_pairs_kdtree(set_a, set_b, epsilon):
    tree_b = KDTree(set_b) 
    close_pairs = []
    for point_a in set_a:
        indices = tree_b.query_ball_point(point_a, epsilon)
        for idx in indices:
            point_b = set_b[idx]
            close_pairs.append((point_a, point_b))
    return close_pairs


if __name__ == "__main__":
  
    m = 1000 # Can change this value
    n = 1000 # Can change this value
    epsilon = 15   # Threshold distance (could be changed)

    
    set_a = generate_random_cord(m)
    set_b = generate_random_cord(n)

    pairs = find_pairs_kdtree(set_a, set_b, epsilon)

    print(f"{Fore.RED}Pairs of points where distance is less than {epsilon}:{Style.RESET_ALL}")
    for pair in pairs:
        distance = euclidean_distance(pair[0], pair[1])
        print(f"{Fore.YELLOW}A: {pair[0]}, {Fore.YELLOW}B: {pair[1]}{Style.RESET_ALL}, {Fore.GREEN}Distance: {distance:.2f}{Style.RESET_ALL}")
