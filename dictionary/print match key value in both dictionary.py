# match key_values in both dictionaries

def match_key_value(d1,d2):
    for key1,value1 in d1.items():
        for key2,value2 in d2.items():
            if key1 == key2 and value1 == value2:
                print(key1,':',value1,'is present in both dictionary')
            else:
                continue
    return
# function call
match_key_value({'key1': 1, 'key2': 2, 'key3': 2,'key':12},{'key1': 1, 'key2': 2})
match_key_value({'1':12,'5':42,'6':56,'7':49,'0':00},{'0':00,'8':64,'1':44,'5':42,'3':49})
