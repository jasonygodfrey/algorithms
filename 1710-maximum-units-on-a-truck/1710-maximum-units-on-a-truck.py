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
