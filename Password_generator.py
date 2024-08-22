import random
import string
def pwgenerator():
  PWUPP = random.SystemRandom().choice(string.ascii_uppercase)
  PWLOW = random.SystemRandom().choice(string.ascii_lowercase)
  PWLOW2 = random.SystemRandom().choice(string.ascii_lowercase)
  PWLOW3 = random.SystemRandom().choice(string.ascii_lowercase)
  PWDIG = random.SystemRandom().choice(string.digits)
  PWDIG2 = random.SystemRandom().choice(string.digits)
  PWDIG3 = random.SystemRandom().choice(string.digits)
  PWSPEC = random.SystemRandom().choice('!@*(§')
  PWD = None
  PWD = random.SystemRandom().choice(random.SystemRandom().choice(string.ascii_uppercase), random.SystemRandom().choice(string.ascii_lowercase), random.SystemRandom().choice(string.digits), random.SystemRandom().choice('!@*(§'))
  PWD = ''.join(random.sample(PWD,len(PWD)))
  return(PWD)



def dynamicPW(length):
  password = ""
  for i in range(length):
    rand_result = [0,0,0,0]
    rand_result[0] = random.SystemRandom().choice(string.ascii_uppercase)
    rand_result[1] = random.SystemRandom().choice(string.ascii_lowercase)
    rand_result[2] = random.SystemRandom().choice(string.digits)
    rand_result[3] = random.SystemRandom().choice('!@*(§')
    password = password + rand_result[random.randint(0,3)]
  return(password)


print(dynamicPW(12))