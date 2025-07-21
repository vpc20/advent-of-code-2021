def binary_search(haystack, needle):
    lo = 0
    hi = len(haystack) - 1
    mid = (lo + hi) // 2

    while lo <= hi:
        if haystack[mid] == needle:
            return True
        elif haystack[mid] > needle:
            hi = mid - 1
        else:
            lo = mid + 1
        mid = (lo + hi) // 2


    return False


assert binary_search([2, 5, 9, 13, 16], 1) == False
assert binary_search([2, 5, 9, 13, 16], 2) == True
assert binary_search([2, 5, 9, 13, 16], 3) == False
assert binary_search([2, 5, 9, 13, 16], 4) == False
assert binary_search([2, 5, 9, 13, 16], 5) == True
assert binary_search([2, 5, 9, 13, 16], 6) == False
assert binary_search([2, 5, 9, 13, 16], 7) == False
assert binary_search([2, 5, 9, 13, 16], 8) == False
assert binary_search([2, 5, 9, 13, 16], 9) == True
assert binary_search([2, 5, 9, 13, 16], 10) == False
assert binary_search([2, 5, 9, 13, 16], 11) == False
assert binary_search([2, 5, 9, 13, 16], 12) == False
assert binary_search([2, 5, 9, 13, 16], 13) == True
assert binary_search([2, 5, 9, 13, 16], 14) == False
assert binary_search([2, 5, 9, 13, 16], 15) == False
assert binary_search([2, 5, 9, 13, 16], 16) == True
assert binary_search([2, 5, 9, 13, 16], 17) == False
assert binary_search([2, 5, 9, 13, 16], 18) == False

assert binary_search([5], 3) == False
assert binary_search([5], 4) == False
assert binary_search([5], 5) == True
assert binary_search([5], 6) == False
assert binary_search([5], 7) == False

assert binary_search([5, 8], 3) == False
assert binary_search([5, 8], 4) == False
assert binary_search([5, 8], 5) == True
assert binary_search([5, 8], 6) == False
assert binary_search([5, 8], 8) == True
assert binary_search([5, 8], 9) == False
assert binary_search([5, 8], 10) == False
