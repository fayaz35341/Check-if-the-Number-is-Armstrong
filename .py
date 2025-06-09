# print("Become the programmer you're meant to be!")
class Sol:
    def arm(self,n):
        a="".join(list(str(n)))
        count=0
        for i in range(len(a)):
            count+=(int(a[i])**(len(a)))
        return n==count
print(Sol().arm(153))
  
