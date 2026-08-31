import cProfile
import pstats
import io
from slow_sort import bubble_sort, find_duplicates
import random

if __name__ == '__main__':
    data = [random.randint(1, 1000) for _ in range(5000)]
    
    pr = cProfile.Profile()
    pr.enable()
    
    sorted_data = bubble_sort(data[:])
    dups = find_duplicates(data[:])
    
    pr.disable()
    
    s = io.StringIO()
    ps = pstats.Stats(pr, stream=s).sort_stats('cumulative')
    ps.print_stats()
    print(s.getvalue())