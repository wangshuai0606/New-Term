from merge_sort import merge_sort

def test_merge_sort():
    assert merge_sort([3, 1, 4, 1, 5, 9, 2, 6]) == [1, 1, 2, 3, 4, 5, 6, 9]
    assert merge_sort([]) == []
    assert merge_sort([1]) == [1]
    assert merge_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

if __name__ == '__main__':
    test_merge_sort()
    print('All tests passed!')
