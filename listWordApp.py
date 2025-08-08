# List of words
words = ["python", "code", "developer", "AI", "chatbot", "data", "science"]

# List comprehension to keep only words with an odd number of characters
odd_length_words = [word for word in words if len(word) % 2 != 0]

# Display results
print("Original list:", words)
print("Words with odd number of characters:", odd_length_words)
