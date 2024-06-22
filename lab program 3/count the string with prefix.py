words = ["pay", "attention", "practice", "attend"]
pref = "at"

count = sum(1 for word in words if word.startswith(pref))
print(count)