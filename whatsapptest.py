from messager.email.models import Category, Customer, Type
from messager.messager import send
from scheduler.watcher import start_watching

if __name__ == "__main__":
      '''
      customer = Customer('Osvaldo','osvaldo020213@gmail.com',[],Category.STUDENT)
      send('email',customer=customer)
      print('Hecho')
      '''
      start_watching()




