
disignation = []
codes = []

data = ("O!","Megacom",  "0705", "Beeline", "0550", "0770", "Katel", "0510", "Fonex", "0543")
for i in data:
    if len(i) == 4 :
        codes.append(i)
    else:
        disignation.append(i)
operators = dict(zip(disignation, codes))
print(codes)
print(disignation)
del operators ['Fonex']
del operators ['Katel']
print(operators)
operators["O!"] = {"0709", "0700", "0707"}
operators["Megacom"] = {"0556","0551","0558"}
operators["Beeline"] = {"0779","0773","0775"}
print(operators)
list_keys = list(operators.keys())
list_keys.sort()
for i in list_keys:
    print(i, '-', operators[i])





























