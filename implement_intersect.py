# set1 & set2 → O(min(len(set1), len(set2)))

# intersection using set comprehension
def intersect_comprehension(A, B):
    return set(a for a in A if a in B)

# intersection using explicit loop
def intersect_loop(A, B):
    C = set()
    for a in A:
        if a in B:
            C.add(a)
    return C

def test_set():
    """Test both intersection implementations with 4 test cases"""
    test_cases = [
        (set(range(10)), set(range(5))),  # Overlapping sets
        (set(), set(range(5))),           # Empty first set
        (set(range(5, 10)), set(range(10))),  # Overlapping sets
        (set(range(3)), set(range(3, 6)))     # Non-overlapping sets
    ]
    
    for i, (A, B) in enumerate(test_cases, 1):
        expected = A & B
        result_comp = intersect_comprehension(A, B)
        result_loop = intersect_loop(A, B)
        
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