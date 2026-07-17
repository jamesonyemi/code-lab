"""
Trapping Rain Water
Level: Hard

Given an array height where height[i] represents the elevation at index i, 
compute how much water can be trapped after raining.

Example:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The trapped water is illustrated by the elevation map, totaling 6 units of water.

    Time Complexity: O(N)
    Space Complexity: O(1)
    
"""

"""
    Where N is the length of the input array.

    Algorithm (Two-Pointer Technique -> Pseudocode):

    FUNCTION trap_rain_water(height_array):
    // Step 3.1: Handle edge case for empty or tiny arrays
    IF height_array is empty THEN
        RETURN 0
    ENDIF

    // Step 3.2: Initialize extreme boundaries
    INITIALIZE left TO 0
    INITIALIZE right TO length(height_array) - 1

    // Step 3.3: Track the highest walls discovered from each boundary
    INITIALIZE left_max TO height_array[left]
    INITIALIZE right_max TO height_array[right]
    INITIALIZE total_water TO 0

    // Step 3.4: Converge pointers toward the center
    WHILE left < right DO

        // Evaluate which boundary acts as the current global bottleneck
        IF left_max < right_max THEN
            
            // Advance left pointer to evaluate the adjacent valley
            INCREMENT left BY 1
            
            // Update the running peak for the left side
            SET left_max TO maximum_of(left_max, height_array[left])
            
            // Accumulate water (guaranteed >= 0 because left_max >= height_array[left])
            ACCUMULATE (left_max - height_array[left]) INTO total_water

        ELSE
            
            // Advance right pointer to evaluate the adjacent valley
            DECREMENT right BY 1
            
            // Update the running peak for the right side
            SET right_max TO maximum_of(right_max, height_array[right])
            
            // Accumulate water
            ACCUMULATE (right_max - height_array[right]) INTO total_water

        ENDIF

    ENDWHILE

    // Step 3.5: All valleys processed
    RETURN total_water
ENDFUNCTION
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
