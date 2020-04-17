# @param {String} s
# @param {Integer[][]} shift
# @return {String}
def string_shift(s, shift)

    x=0    
    until x==shift.length do
        if(shift[x][0]==0)
            y=0
            until y==shift[x][1] do
                s+=s[0]
                s.slice!(0)
                y=y+1
            end
        end

        if(shift[x][0]==1)
            y=0
            until y==shift[x][1] do
                s.insert(0,s[s.length-1])
                s.slice!(s.length-1)
                y=y+1
            end
        end
        x=x+1
    end

    return s
end

# Example:
# Input: s = "abc", shift = [[0,1],[1,2]]
# Output: "cab"
# Explanation: 
# [0,1] means shift to left by 1. "abc" -> "bca"
# [1,2] means shift to right by 2. "bca" -> "cab"

# Constraints:
# 1 <= s.length <= 100
# s only contains lower case English letters.
# 1 <= shift.length <= 100
# shift[i].length == 2
# 0 <= shift[i][0] <= 1
# 0 <= shift[i][1] <= 100