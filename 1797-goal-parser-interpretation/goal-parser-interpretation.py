class Solution(object):
    def interpret(self, command):
        result = ""
        i = 0

        while i < len(command):
            if command[i] == "G":
                result += "G"
                i += 1
            elif command[i:i+2] == "()":
                result += "o"
                i += 2
            elif command[i:i+4] == "(al)":
                result += "al"
                i += 4
        return result 
        