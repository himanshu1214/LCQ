class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        traverse_list = [0, 0, 0]
        print(traverse_list)
        for i in range(len(instructions)):

            if instructions[i] == 'G':
                if i == 0:
                    traverse_list[0] += 1
                    # print(f"Check the enterance: {i} and {traverse_list[i][0]}")
                else:
                    if traverse_list[2] in [90, -270]: 
                        traverse_list[1] = traverse_list[1] - 1
                    if traverse_list[2] in [180, -180]: 
                        traverse_list[0] = traverse_list[0] - 1
                    if traverse_list[2] in [-90, 270]: 
                        traverse_list[1] = traverse_list[1] + 1
                    if traverse_list[2] == 0: 
                        # print(f"Check the enterance: {i} and {traverse_list[i][0]}")
                        traverse_list[0] = traverse_list[0] + 1


            if instructions[i] == 'L':
                traverse_list[2] -= 90

            if instructions[i] == 'R':
                traverse_list[2] += 90
            print(f"INDEX: {i} and x: {traverse_list[0]} and y : {traverse_list[1]} and {traverse_list[2]}")
            print(f"INST: {instructions[i]}")

            if abs(traverse_list[2])>= 360:
                if traverse_list[2]<= -360:
                    traverse_list[2] = traverse_list[2]%360*(-1)
                else:
                    traverse_list[2] = traverse_list[2]%360

            print(traverse_list[2])    
        if traverse_list[2] != 0 or traverse_list[:2]==[0, 0]:
            return True
        else:
            return False
