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
