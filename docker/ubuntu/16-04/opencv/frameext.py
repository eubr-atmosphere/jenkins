#!/usr/bin/python

import cv2
import sys, getopt

def main(argv):
   inputfile = ''
   outputfile = ''
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
   except getopt.GetoptError:
      print 'frameext.py -i <MP4 inputfile> -o <outputfileprefix>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'frameext.py -i <MP4 inputfile> -o <outputfileprefix>'
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputfileprefix = arg
   print 'Input file is "', inputfile, '"'
   print 'Output file is "', outputfileprefix, '"'
   extract(inputfile, outputfileprefix)


def extract(inputfile, outputprefix):
  print 'OpenCV version: ', cv2.__version__
  vidcap = cv2.VideoCapture(inputfile)
  success,image = vidcap.read()
  count = 0
  success = True
  while success:
    cv2.imwrite("%s%d.jpg" %(outputprefix, count), image)     # save frame as JPEG file
    success,image = vidcap.read()
#    print 'Read a new frame: ', success
    count += 1
    
if __name__ == "__main__":
   main(sys.argv[1:])


