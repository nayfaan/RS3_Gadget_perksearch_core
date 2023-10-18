from itertools import product
from tqdm import tqdm

def generate_permutations_with_progress(iterable, r):
    total_permutations = len(list(product(iterable, repeat=r)))
    with tqdm(total=total_permutations) as pbar:
        for perm in product(iterable, repeat=r):
            # Process each permutation here
            # For demonstration purposes, we'll just print the permutation
            # print(perm)
            pbar.update(1)  # Update progress bar for each permutation

# Example usage
elements = ['A', 'B', 'C']
permutation_length = 15

generate_permutations_with_progress(elements, permutation_length)
