import re
import csv

# this was manually pulled from html on adwords for the range feb 13, 2010 to jul 13, 2017
# there should be one observation per day

# variables are: conversions, mean days to conversion, ad clicks per conversion,
#   and ad impressions per conversion


file = open('html_text').read().split("\n")

# how could I do this print loop in one line??
for x in file:
    print x
print len(file)

# these are the number of conversions
if file[0]: numbers = re.findall('>([0-9]+?)<', file[0])

print numbers
print len(numbers), type(numbers[0]) # is a list of strings

if file[1]: numbers1 = re.findall('>([0-9.]+?)<', file[1])
print numbers1
print len(numbers1), type(numbers1[0])


for x in range(len(numbers)):
    numbers[x] = int(numbers[x])
for x in range(len(numbers)):
    numbers1[x] = float(numbers1[x])

print type(numbers[0]), type(numbers1[0])

# adding clicks per conversion and impressions per conversion
if file[2]:numbers2 = re.findall('>([0-9.]+?)<', file[2])
print 'this is numbers2:', numbers2
print len(numbers2)
if file[3]: numbers3 = re.findall('>([0-9.]+?)<', file[3])
print 'this is numbers3:', numbers3
print len(numbers3)

for x in range(len(numbers2)):
    numbers2[x] = float(numbers2[x])
for x in range(len(numbers3)):
    numbers3[x] = float(numbers3[x])


dlist = list()
for x in range(len(numbers)):
    d = dict()
    d['conv'] = numbers[x]
    d['dtc'] = numbers1[x]
    d['cpc'] = numbers2[x]
    d['ipc'] = numbers3[x]
    dlist.append(d)
print len(dlist)

tuplist = list()
for x in dlist:
    conv = x['conv']
    dtc = x['dtc']
    cpc = x['cpc']
    ipc = x['ipc']
    tup = (conv, dtc, cpc, ipc)
    tuplist.append(tup)
    # tuplist += tuple((x['conv']), (x['dtc']))
print tuplist
print len(tuplist)

with open('dtc.csv', 'w') as out:
    csv_out = csv.writer(out)
    csv_out.writerow(['conversions', 'days2conv', 'cpc', 'ipc'])
    for row in tuplist:
        csv_out.writerow(row)
