#find sum of given values passing variable number of arguments
def input_list(**m):
    sum=0
    for x,y in m.items():
        sum+=  y 
    print(sum)
input_list(id1=100,id2=200,id3=300)