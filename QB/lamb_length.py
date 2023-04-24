weekdays=['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
days=filter(lambda x:x if len(x)==6 else '',weekdays)
for d in days:
    print(d)
