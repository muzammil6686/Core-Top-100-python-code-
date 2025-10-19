def vowels_count(s):
    count = 0
    vowels = "aeiouAEIOU"
    for char in s:
        if char in vowels:
            count += 1
    print(count) 


vowels_count("Hello World")
vowels_count("Programming")
vowels_count("OpenAI")