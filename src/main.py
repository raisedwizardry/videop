from server.instance import server
import sys
import os

# Need to import all resources
# so that they register with the server
#from resources.book import *
from resources.episode import *
from resources.recordings import *

if __name__ == '__main__':
    server.run()
