with open('19.txt', 'r') as file:
    towels, designs = file.read().strip().split("\n\n")
towels = [towel.strip() for towel in towels.split(",")]
designs = designs.split("\n")

def match_towels(design):
    dp = [False] * (len(design) + 1)
    dp[0] = True 
    for i in range(1, len(design) + 1):
        for towel in towels:
            if i >= len(towel) and dp[i - len(towel)] and design[i - len(towel):i] == towel:
                dp[i] = True
                break 
    return dp[len(design)]

count = 0
for design in designs:
    if match_towels(design):
        count += 1
print(count)
