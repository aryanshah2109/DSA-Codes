# Return the largest odd number in the given string of numbers
# If no odd number found, return empty string
# Eg: "13526" => 135
# Eg: "1569287" => 1569287
# Eg: "2046" => ""

def largestOddNo(num: str):
    if len(num) == 0:
        return ""

    n = len(num)

    for i in range(n-1, -1, -1):
        if int(num[i]) % 2 != 0:
            return num[0:i+1]
    
    return ""

print(largestOddNo("13526"))
print(largestOddNo("1569287"))
print(largestOddNo("2046"))