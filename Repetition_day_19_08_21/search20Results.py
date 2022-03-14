try:
    from googlesearch import search
except ImportError:
    print('No module named google found.')

queries = ['2nd officer DPO job','DPO marine job','2nd mate DPO job','HSE work in rafineries']

for query in queries:
    count = 0
    for j in search(query,tld='com',num=20, stop=20,pause=3):
        count += 1
        print('Looking for: ',query)
        print(count,'.',j)