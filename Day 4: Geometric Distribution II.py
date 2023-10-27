# Enter your code here. Read input from STDIN. Print output to STDOUT
def Geometric(n,p):
    return (1-p)**(n-1) * p

nume,deno = list(map(int,input().split()))
n = int(input())

print(f"{sum([Geometric(i,nume/deno) for i in range(1,n+1)]):.3f}")