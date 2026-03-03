#first
numbers = [5, 12, 3, 18, 7, 25, 1, 14]
print(numbers[0])
print(numbers[2])
print(numbers[-1])
max=0
for i in numbers:
    if i>max:
        max=i
print(f"max: {max}")
numbers.append(100)
numbers.remove(3)
print (*numbers)

#second
text=input("Print string ")
unique_chars=set(text)
print(' , '.join(unique_chars))

#third
phonebook = {
    "Алиса": "123-45-67",
    "Борис": "234-56-78"
}
phonebook["Виктор"] = "345-67-89"
name = "Борис"
print(f"Phone number of {name}: {phonebook[name]}")
for name, number in phonebook.items():
    print(name," - ", number)

#forth
data = [1, 4, 7, 8, 10, 3, 12, 15]
squares=[x**2 for x in data]
even=[x**2 for x in data if (x%2==0)]
strings=[str(x) for x in data]
print("Квадраты:", squares)
print("Квадраты четных:", even)
print("Строки:", strings)

#fifth
string=input("Input string of words: ").lower()
words=string.split()
word_count={}
for i in words:
    if i in word_count:
        word_count[i]+=1
    else:
        word_count[i]=1
for w, c in word_count.items():
    print(f"{w}: {c}")
