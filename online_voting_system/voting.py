candidates=["Raj","Vijay","Ajay","Ravi"]

votes={candidate : 0 for candidate in candidates}#Dict comphrehension
num_voters=int(input("Enter the number of voters: "))

for i in range(num_voters):
    print(f"\nVoter {i+1}")#Iterating over voters
    print("Candidates:",", ".join(candidates))
    vote=input("Choose your candidate: ")