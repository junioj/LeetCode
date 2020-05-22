class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if(coordinates[0][0]!=coordinates[1][0]):
            slope = (coordinates[0][1]-coordinates[1][1])/(coordinates[0][0]-coordinates[1][0])
        else:
            for x in coordinates:
                if x[0]!=coordinates[0][0]:
                    return False
                
        yint = (coordinates[0][1])-slope*coordinates[0][0]
        
        for x in coordinates:
            if(x[1]!=slope*x[0]+yint):
                return False
        
        return True

# Problem: You are given an array coordinates, coordinates[i] = [x, y], 
# where [x, y] represents the coordinate of a point. Check if these 
# points make a straight line in the XY plane.