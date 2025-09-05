candidates=["Raj","Vijay","Ajay","Ravi"]

votes={candidate : 0 for candidate in candidates}#Dict comphrehension
num_voters=int(input("Enter the number of voters: "))

for i in range(num_voters):
    print(f"\nVoter {i+1}")#Iterating over voters
    print("Candidates:",", ".join(candidates))
    vote=input("Choose your candidate: ")

    if vote in votes:#Inc vote of candidate whom u voted
        votes[vote]+=1
        print(f"Vote casted for {vote} successfully!")
    else:
        print("Invalid candidate! Vote not counted.")

print("\n-----Voting Results-----")
for candidate, count in votes.items():
    print(f"{candidate}: {count} votes")

max_votes=max(votes.values())

winners=[name for name, votes in votes.items() if votes==max_votes]#Cond to calculate winner
if len(winners)==1:
    print(f"The winner is {winners[0]} with {max_votes} votes!")
else:
    print("It's a tie between:", ", ".join(winners), f"with {max_votes} votes each!")