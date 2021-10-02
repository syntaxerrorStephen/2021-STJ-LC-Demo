# Example code for Thingspeak, ensure correct write API key is linked
# Based around demo LC2022 project
import sys 
from urllib.request import urlopen
from time import sleep

def setup():
  #bool_arg = "Yes"

  sleep(60)

 # bool_arg = input("Is the bin out?: ")

  if bool_arg == "Yes":
    pos()
  else:
    neg()

def pos():
  f = urlopen("https://api.thingspeak.com/update?api_key=ZBQPUJOQEZB2SHUD&field1=1") 
    #print(f.read())
  f.close()
  setup()

def neg():
  f = urlopen("https://api.thingspeak.com/update?api_key=ZBQPUJOQEZB2SHUD&field1=2") 
    #print(f.read())
  f.close()
  setup()

bool_arg = "Yes"

setup()
