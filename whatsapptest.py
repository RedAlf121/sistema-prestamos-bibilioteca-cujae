import pywhatkit

from messager.email.models import Category, Customer, Type
from messager.messager import send

#pywhatkit.sendwhatmsg(phone_no='+5356707158',message='pareces un singao comepinga hablando solo mi tanke',time_hour=23, time_min=54)

if __name__ == "__main__":
      customer = Customer('Osvaldo','osvaldo020213@gmail.com',[],Category.STUDENT)
      send('email',customer=customer)
      print('Hecho')



