teams = 4096
matches = 0

while teams != 1:
    teams = teams // 2
    matches += teams

print(matches)