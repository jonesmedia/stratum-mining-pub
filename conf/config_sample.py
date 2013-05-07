'''
This is example configuration for Stratum server.
Please rename it to settings.py and fill correct values.
'''

# ******************** GENERAL SETTINGS ***************

# Enable some verbose debug (logging requests and responses).
# Turn this off once ready to go live  -  True|False
DEBUG = True

# Destination for application logs, files rotated once per day.
# log in current directory - ensure log directory exists
LOGDIR = 'log/'

# Main application log file.
LOGFILE = 'stratum.log'

# Possible values: DEBUG, INFO, WARNING, ERROR, CRITICAL
# Turn this to INFO once ready to go live
LOGLEVEL = 'DEBUG'

# How many threads use for synchronous methods (services).
# 30 is enough for small installation, for real usage
# it should be slightly more, say 100-300.
THREAD_POOL_SIZE = 300


#Not sure what this is.. lol
ENABLE_EXAMPLE_SERVICE = True

# ******************** TRANSPORTS *********************
# Hostname or external IP to expose
HOSTNAME = 'localhost'

# Port used for Socket transport. Use 'None' for disabling the transport.
LISTEN_SOCKET_TRANSPORT = 3333

# Port used for HTTP Poll transport. Use 'None' for disabling the transport
LISTEN_HTTP_TRANSPORT = None

# Port used for HTTPS Poll transport
LISTEN_HTTPS_TRANSPORT = None

# Port used for WebSocket transport, 'None' for disabling WS
LISTEN_WS_TRANSPORT = None

# Port used for secure WebSocket, 'None' for disabling WSS
LISTEN_WSS_TRANSPORT = None

# Hostname and credentials for one trusted Bitcoin node ("Satoshi's client").
# Stratum uses both P2P port (which is 8333 already) and RPC port
#update this information - user/password from ~/.litecoin/litecoin.conf
LITECOIN_TRUSTED_HOST = 'localhost'
LITECOIN_TRUSTED_PORT = 8332
LITECOIN_TRUSTED_USER = 'user'
LITECOIN_TRUSTED_PASSWORD = 'somepassword'

# Use "echo -n '<yourpassword>' | sha256sum | cut -f1 -d' ' "
# for calculating SHA256 of your preferred password
ADMIN_PASSWORD_SHA256 = None
#ADMIN_PASSWORD_SHA256 = '9e6c0c1db1e0dfb3fa5159deb4ecd9715b3c8cd6b06bd4a3ad77e9a8c5694219' # SHA256 of the password

IRC_NICK = None

# MYSQL connection details

DATABASE_HOST = ''
DATABASE_DBNAME = ''
DATABASE_USER = ''
DATABASE_PASSWORD = ''

# Memcache server host and port
MEMCACHE_HOST = 'localhost:11211'

# Memcache authorization timeout - in seconds
MEMC_AUTH_TIMEOUT = 900


# Pool related settings
# to get central_wallet address: bitcoind/litecoind getaccountaddress ""

INSTANCE_ID = 31
CENTRAL_WALLET = 'Your_Valid_Bitcoin_or_Litecoin_Address'
PREVHASH_REFRESH_INTERVAL = 5 # in sec
MERKLE_REFRESH_INTERVAL = 60 # How often check memorypool
COINBASE_EXTRAS = '/stratum/'
