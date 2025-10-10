# set1 | set2 → O(len(set1) + len(set2))

# union using set comprehension
import itertools


def union_comprehension(A, B):
    return set(itertools.chain(A, B))

# union using explicit loop
def union_loop(A, B):
    C = set()
    for a in A:
        C.add(a)
    for b in B:
        C.add(b)
    return C

def test_set():
    """Test both union implementations with 4 test cases"""
    test_cases = [
        (set(range(10)), set(range(5))),  # Overlapping sets
        (set(), set(range(5))),           # Empty first set
        (set(range(5, 10)), set(range(10))),  # Overlapping sets
        (set(range(3)), set(range(3, 6)))     # Non-overlapping sets
    ]
    
    for i, (A, B) in enumerate(test_cases, 1):
        expected = A | B
        result_comp = union_comprehension(A, B)
        result_loop = union_loop(A, B)
        
        print(f"Test case {i}: A={A}, B={B}")
        print(f"  Expected: {expected}")
        print(f"  Comprehension: {result_comp} ✓" if result_comp == expected else f"  Comprehension: {result_comp} ✗")
        print(f"  Loop: {result_loop} ✓" if result_loop == expected else f"  Loop: {result_loop} ✗")
        print()
        
        # Assertions
        assert expected == result_comp, f"Comprehension failed for test case {i}"
        assert expected == result_loop, f"Loop failed for test case {i}"

if __name__ == "__main__":
    test_set()