#!/usr/bin/python
import crypt
import csv
hashes = []
salts = []
with open('hash.txt') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=':')
    for row in readCSV:
    	somehash = row[1]
	hashes.append(somehash)
with open('hash.txt') as csvfile:
    readCSV = csv.reader(csvfile, delimiter='$')
    for row in readCSV:
	somesalt = "$" + row[1]
	somesalt += "$" + row[2]
	salts.append(somesalt)
for entry in open("/home/jose/passwdlists/rockyou.txt") :
	entry = entry.rstrip("\n")
        i = 0
	for elem in hashes:
		curhash = crypt.crypt(entry, salts[i])
		print "PASSWORD: " + entry + " HASH: " + curhash
		if curhash == elem:
			print "Hey Boss., I think I found your password\nANSWER: " + entry + " HASH: " + curhash
			hashes.remove(elem)
			salts.remove(salts[i])
			break
		i += 1
	if len(hashes) == 0 :
		break
