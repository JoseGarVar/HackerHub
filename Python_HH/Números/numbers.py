"""

Challenger - http://www.ooyala.com/mx/careers/sg

"""
import sys

class NumberToLetters:
  def __init__(self):
    self.unidades = {0:'cero',1:'uno', 2:'dos', 3:'tres', 4:'cuatro', 5:'cinco', 6:'seis', 7:'siete', 8:'ocho', 9:'nueve'}
    self.before = {10:'diez', 11:'once', 12:'doce', 13:'trece', 14:'catorce', 15:'quince', 16:'dieciseis',17:'diecisiete', 18:'dieciocho', 19:'diecinueve', 20:'veinte'}
    self.decenas = {20:'veinti', 30:'treinta', 40:'cuarenta', 50:'cincuenta', 60:'sesenta', 70:'setenta', 80:'ochenta', 90:'noventa', 100:'cien'}
    self.centenas = {100:'ciento', 200:'doscientos', 300:'trecientos', 400:'cuatrocientos', 500:'quinientos', 600:'seiscientos', 700:'setecientos', 800:'ochocientos', 900:'novecientos'}

    self.ls = []

  def get_number(self, number):

    if number < 1000:
      n = self._digits(number)
      if not n:
        self._set_str(self.unidades, number)
      elif n >= 1 and n < 10:
        numbers = dict(self.unidades.items() + self.before.items() + self.decenas.items() )
        self._set_str(numbers, number)
      elif n >= 10:
        numbers = dict(self.unidades.items() + self.before.items() + self.decenas.items() + self.centenas.items())
        self._set_str(numbers, number)      
      
      print sorted(self.ls)
      
    else:
      print "Number minor to 1000, please!"
  
  def _set_str(self, numbers, number):
    for k,v in numbers.items():
      if k <= number:
        for c in list(v):
          if not c in self.ls:
            self.ls.append(c)
            
  def _digits(self, number):
    if number != 0:
      number = number / 10
      self._digits(number)
      return number
      
if __name__ == '__main__':
  if len(sys.argv) < 2 or len(sys.argv) > 2:
    print "Usage: \n\t python numbers.py {number}"
    sys.exit(1)
  elif len(sys.argv) == 2:
    number = int(sys.argv[1])
    ntl = NumberToLetters()
    ntl.get_number(number)
  