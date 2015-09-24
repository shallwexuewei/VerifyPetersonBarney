
file = open('verified_pb.data', 'r')
lines = file.readlines()
num2ascii = {}
num2fsum = {}
num2cnt = {}
for line in lines:
    entries =  line.split('\t')
    
    phoneme_number = entries[2]
    phoneme_ascii = entries[3].replace('*', '')
    if phoneme_number not in num2ascii.keys():
        num2ascii[phoneme_number] = phoneme_ascii
    elif num2ascii[phoneme_number] != phoneme_ascii:
        print "error!"
    fs = [0 for i in range(4)]
    for i in range(4):
        fs[i] = int(entries[4+i].replace('.', '').replace('\n', ''))
    
    if phoneme_number not in num2fsum.keys():
        num2fsum[phoneme_number] = fs
        num2cnt[phoneme_number] = 1
    else:
        for i in range(4):
            num2fsum[phoneme_number][i] += fs[i]
            num2cnt[phoneme_number] += 1
        
print num2ascii
print num2fsum
print num2cnt

for phoneme_num in num2ascii.keys():
    print num2ascii[phoneme_num],
    for i in range(4):
        print float(num2fsum[phoneme_num][i])/num2cnt[phoneme_num],
    print 
