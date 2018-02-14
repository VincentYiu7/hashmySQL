import hashlib
name =[
    'root', 
    'pma', 
    'Alice', 
    'Bob' 
    'Carol' 
    'David' 
    'Evan' 
    'Flynn'
   ]
ps = [
    'd35db127db631e6e27c6b75e8d376b04f64faf83',	#helloworld
    'c2d24dca38e9e862098b85bf0ab35caa52803797',	#abcdef
    '81101ded975d54bd76a3c8ead293597ae9bb143f',	#computer
    '1fdb0d828172183735f1ed9e45e6af3ce04de9d1',	#security
    '2470c0c06dee42fd1618bb99005adca2ec9d1e19',	#password
    '6063c78456bb048baf36be1104d12d547834dfea',	#qwertyuiop
    'ce6b124c2f3d90ca4dee06d35b81ff3a9a22ee32',
    'd5d82ef0b0a344a314e3b3e8d1e78a4697b97a53'
]
print('Username : Password')
with open('dict.txt', 'r') as inF:
    for line in inF: 
        data = line.rstrip('\n')
        hash_object = hashlib.sha1(data.encode('utf-8'))
        hash_object = hashlib.sha1(hash_object.digest())
        hex_dig = hash_object.hexdigest()
        if hex_dig in ps: print(name[ps.index(hex_dig)], data)