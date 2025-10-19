def vowels(word):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    if word[0] in vowels:
        print("Yes")
    else:
        print("No")


vowels("Apple")
vowels("banana")
vowels("Orange")
vowels("grape")
vowels("umbrella")