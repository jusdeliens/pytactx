from dotenv import dotenv_values
import getpass

env = dotenv_values(".env") 

ROBOTID = env['ROBOTID'] if 'ROBOTID' in env else input("👾 robotId: ")
ARENA = env['ARENA'] if 'ARENA' in env else input("🎲 arena: ")
BROKERADDRESS = env['BROKERADDRESS'] if 'BROKERADDRESS' in env else input("🌐 server: ")
BROKERPORT = int(env['BROKERPORT']) if 'BROKERPORT' in env else int(input("📭 port: "))
USERNAME = env['USERNAME'] if 'USERNAME' in env else input("👤 username: ")
PASSWORD = env['PASSWORD'] if 'PASSWORD' in env else getpass("🔑 password: ")
VERBOSITY = int(env['VERBOSITY']) if 'VERBOSITY' in env else int(input("🪲 verbosity: "))