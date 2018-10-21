# Psuedo-code 
-This approach is the exact same as the approach where you take the earliest    finish time of each activity to come to the optimal solution, just inverted. So instead of picking the earliest finish time from the front, you pick the earliest start time from the back. It sorts by starting time from last to first. picks the first activity (I) from that list. Nullifies any other activity thats during that pick (I)'s run time and picks the next activity based on the ordering of the list. This runs until the list is empty/nullified. 

# Runtime 
-The runtime is dictated by the sorting done at the beginning O(nlogn)


# To run 
``` python greed.py ```
