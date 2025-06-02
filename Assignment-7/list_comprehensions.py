squares_of_evens = [x**2 for x in range(1, 21) if x % 2 == 0]
print(squares_of_evens)

words = ["apple", "cake", "orange", "car", "bike", "strawberry"]
vowels = "aeiou"
filtered_words = [word for word in words if word[0].lower() in vowels]
print("Words starting with a vowel:", filtered_words)
