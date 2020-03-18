# file = open("NewFile.txt","w")
#
# txt = "This is our first txt in file "
# file.write(txt)
# file.close()

# file = open("NewFile.txt","r")
# print(file.readlines())
# file.close()

# file = open("NewFile.txt","a")
# txt = """
# A wiki is run using wiki software,
# otherwise known as a wiki engine.
#  A wiki engine is a type of content management system,
#  but it differs from most other such systems,
#  including blog software, in that the content
#  is created without any defined owner or leader,
#  and wikis have little inherent structure, """
#
# file.write(txt)
# file.close()

import os
#os.rename("NewFile.txt","FileNew.txt")
os.remove("FileNew.txt")
