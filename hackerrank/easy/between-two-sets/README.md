# Approach

1. Begin from largest element in list A - "possible_factor"
2. Check all elements in A area a factor of possible_factor
3. Check all maxA is a factor of all elements in B
4. If 2/3 contain an element violating this - reject possible_factor and move on
5. Add maxA to possible_factor and try steps 2-4 again (factors must be a multiple of maxA)
