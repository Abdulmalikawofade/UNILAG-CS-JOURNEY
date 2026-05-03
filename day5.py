print("=== Day 5: The grind loop ===")

#while loop - keep going until condition falls
days_coding = 1
target_days = 5

print("While loop: Counting your streak")
while days_coding <= target_days:
    print(f"Day {days_coding}: Abdulmalik showed up for himself")
    days_coding += 1
print("STreak complete!")

print("For loop: people who matter")
real_ones = ["Abdulmalik", "Github", "Python", "UNILAG"]
for person in real_ones:
    print(f"shoutout to {person} - real from day 1")
print("\nNotice who is not on that list")
print("Fake friends don't get looped in anymore")

score = 279
print(f"\nCounting up to {score}:")
for i in range(275, score + 1):
    print(f"{i}... still HIM")
