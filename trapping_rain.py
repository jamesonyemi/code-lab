"""
Trapping Rain Water
Level: Hard

Given an array height where height[i] represents the elevation at index i, 
compute how much water can be trapped after raining.

Example:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The trapped water is illustrated by the elevation map, totaling 6 units of water.

"""

def trapping_rain_water(elevations: list[int]) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    arr = elevations

    if not arr:
        return 0
        
    l, r = 0, len(arr) - 1
    l_mx = arr[l]
    r_mx = arr[r]
    wt = 0

    while l < r:
        if l_mx < r_mx:
            l += 1
            l_mx = max(l_mx, arr[l])
            wt += l_mx - arr[l]
            
        else:
            r -= 1
            r_mx = max(r_mx, arr[r])
            wt += r_mx - arr[r]
        
    return wt


if __name__ == "__main__":
    elevations = [int(x) for x in input().split()]
    res = trapping_rain_water(elevations)
    print(res)
