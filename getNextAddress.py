#! /usr/bin/python
from armoryengine import *
wlt = PyBtcWallet().readWalletFile( CLI_ARGS[0] )

f1=open(CLI_ARGS[1], 'w+')

x=0

for x in range (0, int(CLI_ARGS[2])): 
	print >> f1, wlt.getNextUnusedAddress().getAddrStr()
