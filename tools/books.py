import getopt
import os
import sys

def loadBooks(path):
  dirList = os.listdir(path)
  print(dirList)

def main(argv):
  try:
    opts, args = getopt.getopt(argv, "ht:u:b:n:or:c:", ["help", "target=", "usfmDir=", "builtDir=", "name=","oeb","order=","config="])
  except getopt.GetoptError:
    usage()
    sys.exit(2)
  for opt, arg in opts:
    if opt in ("-h", "--help"):
      return usage()
    elif opt in ("-t", "--target"):
      targets =  arg
    elif opt in ("-u", "--usfmDir"):
      usfmDir = arg
    elif opt in ("-b", "--builtDir"):
      buildDir = arg
    elif opt in ("-n", "--name"):
      buildName = arg
    elif opt in ("-r", "--order"):
      order = arg
    elif opt in ("-o", "--oeb"):
      oebFlag = True
    elif opt in ("-c", "--config"):
      config = rendererConfig.RendererConfig(arg, os.path.join(rootdiroftools, 'default.config'))
    else:
      usage()

  loadBooks(usfmDir)    

if __name__ == "__main__":
    main(sys.argv[1:])      