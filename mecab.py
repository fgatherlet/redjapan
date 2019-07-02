import os,os.path,sys
sys.path.append(os.path.join(os.path.dirname(__file__), "lib"))
import jpextract

print(jpextract.extract_noun("よつばと面白いかな。いろんなあれやこれや"))
