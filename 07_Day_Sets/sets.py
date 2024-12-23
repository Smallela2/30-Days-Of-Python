#Exercise level 1
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
print("length", len(it_companies))
it_companies.add("Twitter")
print(it_companies)
companies = ("Capgemini", "Hcl")
it_companies.update(companies)
print(it_companies)
it_companies.discard("Apple")
print("after remove:", it_companies)


#Exercise level 2
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
C = A.union(B)
print(C)
D =A.intersection(B)
print(D)
print(A.issubset(B))
print(A.isdisjoint(B))
print(A.union(B) & B.union(A))
print(A.symmetric_difference(B))
del A
del B


#Exercise level 3
age = [22, 19, 24, 25, 26, 24, 25, 24]
my_set = set(age)
print(my_set)
if len(age) > len(my_set):
    print("age is bigger")
elif len(age) < len(my_set):
    print("my_set is bigger")
else:
    print("Both are Equal")
sentence = "I am a teacher and I love to inspire and teach people."
# Split the sentence into words and convert to a set to get unique words
words = sentence.split()  # Splits the sentence into a list of words
unique_words = set(words)  # Convert the list to a set to remove duplicates
print("Unique words:", unique_words)
print("Number of unique words:", len(unique_words))
