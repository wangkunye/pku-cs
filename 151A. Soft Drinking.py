n,k,l,c,d,p,nl,np=map(int,input().split())
a=[(k*l)//(n*nl),(c*d)//n,p//(n*np)]
print(min(a))