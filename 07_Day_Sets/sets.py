it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
print("length", len(it_companies))
it_companies.add("Twitter")
print(it_companies)
companies = ("Capgemini", "Hcl")
it_companies.update(companies)
print(it_companies)
it_companies.discard("Apple")
print("after remove:", it_companies)


