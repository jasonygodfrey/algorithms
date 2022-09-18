class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda arr: arr[1], reverse=True)
        
        total_units = 0
        for numboxes, unit in boxTypes:
            if truckSize <= numboxes:
                total_units += truckSize * unit
                break
            total_units += numboxes * unit
            truckSize -= numboxes
        
        return total_units
""" The code above does the following, explained in English:
1. sort the list of boxes by unit size from largest to smallest. 
2. iterate through the list, keeping track of how many boxes are left in the truck.
3. if the number of boxes left in the truck is greater than or equal to the number of boxes in the current box type, 
   add the number of boxes times its unit size to the total units. 
4. if the number of boxes left in the truck is less than the number of boxes in the current box type, 
   add the number of boxes left in the truck times its unit size to the total units. 
5. if the number of boxes left in the truck is less than 0, break out of the loop. 
6. return the total units. """