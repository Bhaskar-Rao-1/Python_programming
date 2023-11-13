#dictionary is changable unordered having key and value
#acces value quickly

capitals = {'USA':'Washington DC',
              'India':'New Delhi',
              'China':'Beijing',
              'Russia':'Moscow'}

print(capitals['Russia'])

print(capitals.get('Germny'))#if we use capitals['Germany'] getting error

capitals.update({'Germany':'Berlin'})#by using upate you can also change existed value
print(capitals.keys())

print(capitals.values())

capitals.pop('China')
capitals.clear()
print(capitals.items())#print entire dictionary

for key,value in capitals.items():
    print(key,':',value)

