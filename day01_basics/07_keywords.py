#print the no. of keywords
import keyword
print("Number of keywords:",len(keyword.kwlist))

#print all keywords
#import keyword
print(keyword.kwlist)

#print keywords one by one
#import keyword
for word in keyword.kwlist:
    print(word)