stratum-mining
==============

Demo implementation of litecoin mining pool using Stratum mining protocol -- forked from Slush0
http://github.com/slush0/stratum-mining

Thanks go out to him for creating his version of the Stratum mining protocol and sample files that we
have been able to work through and adapt for litecoin mining.

For Stratum mining protocol specification, please visit http://mining.bitcoin.cz/stratum-mining.

This fork is still a work in progress - once complete, full details will be posted and a link will be shared.


NOTE: ^ - currently it appears that shares are not being pushed back to litecoind and therefore are not being validated. 
If you wish to help improve/debug this, please feel free to contact me at the address below.


This fork should support bitcoin and most alt-coins including scrypt-based coins like litecoin.

Current issue details:
----------------------
So ive put some logging lines into the code to work out what is going on and i think i have narrowed it down to the following

2013-04-09 21:13:43,948 INFO template_registry template_registry.submit_share # Job Target: 114990879509129085127507265365841254673886324032102872501331165184

2013-04-09 21:13:43,948 INFO template_registry template_registry.submit_share # Hash_int: 89220399313991226919392322697890206382314560561523522085963210361529183705087

Thats our problem right there... hash_int !<= job.target and therefore not submitting... so job.target is not right im guessing

Update:
To help, please see the extract from the stratum log:
http://pastebin.com/Jk2wZ9a6
To get extra information, I have changed 'hash_int <= job.target'  to 'hash_int >= job.target'


git clone https://github.com/Tydus/litecoin_scrypt.git
cd litecoin_scrypt
sudo python setup.py install


Contact:
-------
This pool implementation is provided by http://www.viperausmedia.com.au. You can contact
me by email info(at)viperausmedia.com.au.

Donations:
----------
BTC - 1CWmoy4xTSXV8NmiFtz2aCHWfy1ikzaBTM

LTC - LVWjBYNgj9MFPMhm5bMq3tjRCKiKVzMeL1
