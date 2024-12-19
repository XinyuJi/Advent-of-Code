with open('19.txt', 'r') as file:
    data = file.read()
towels, designs = data.strip().split("\n\n")
towels = [towel.strip() for towel in towels.split(",")]
designs = designs.split("\n")

def count_towel_combinations(design, towels):
    dp = [0] * (len(design) + 1)
    dp[0] = 1
    for i in range(1, len(design) + 1):
        for towel in towels:
            if i >= len(towel) and design[i - len(towel):i] == towel:
                dp[i] += dp[i - len(towel)] 
    return dp[len(design)]

total_count = 0
for design in designs:
    total_count += count_towel_combinations(design, towels)
print(total_count)
