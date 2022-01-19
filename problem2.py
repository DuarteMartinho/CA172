#!/usr/bin/env python3

gen = int(input("Which generation would you like: "))

term1 = 0
term2 = 1
i = 1

while i < gen:
    newterm2 = term1 + term2
    # Update t1 with t2
    term1 = term2

    # Update t2 with t1 + t2
    term2 = newterm2

    # close loop
    i += 1
    print(term1)

# print the output
print("There are", term1, "males ancestors in generation", gen)
