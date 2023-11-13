#set is a collection of unordered,unindexed and no duplicate values

utensils = {'fork','spoon','knife','knife'}
dishes = {'bowl','plate','knife','cup'}

utensils.add('napkin')
utensils.remove('fork')
#utensils.clear()
dishes.update(utensils)

dinner_table = utensils.union(dishes)#dishes.union(utensils)

print(utensils.difference(dishes))#what doesnot have in dishes compared to utensils
print()


print(utensils.intersection(dishes))#what common element
print()
for i in dinner_table :
    print(i)