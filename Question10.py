teams = 4096
rounds = 0
print("Starting teams", teams)
while teams != 1:
    teams = teams // 2
    rounds += 1
    print(teams, "teams remaining at the end of round", rounds)

print("Number of Rounds ", rounds)