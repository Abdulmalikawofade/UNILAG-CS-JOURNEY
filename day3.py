name = "Abdulmalik"
jamb_score = 279
UNILAG_cutoff = 200
dream_cutoff = 320

print(f"Checking JAMB status for {name}...")

#decison 1: Did you pass UNILAG cutoff?
if jamb_score >= UNILAG_cutoff: 
    print(f"✅ {name}, you passed UNILAG cutoff! 279 >= 200")
else:
    print(f"❌{name}, you need {UNILAG_cutoff- jamb_score} more points")

#decision 2: Are you at dream score yet?
if jamb_score >= dream_cutoff:
    print(f"🏆 {name}, you hit 320! UNILAG CS is yours")
else: 
    points_needed = dream_cutoff - jamb_score
    print(f"📈 {name}, you need {points_needed} more points for 320")
    print(f"Grind mode: ACTIVATED")

#decision 3: How many years till UNILAG?
current_year = 2026
target_year = 2027
years_left = target_year - current_year

if years_left == 1: print(f"⏰ {name}, only {years_left} year left. Final stretch!")
elif years_left == 0: print(f"🎓 {name}, you should be in UNILAG now!")
else: print(f"📆 {name}, {years_left} years to go. Keep building")