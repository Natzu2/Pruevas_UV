from pyowm import OWM
import sched, time
import csv  

owm = OWM('25e4f8c6b58ce79d30fb2f9f51c1d1a6')
uv_mgr = owm.uvindex_manager()
uv_index = uv_mgr.uvindex_around_coords(27.967115, -110.918797)

# def loop(scheduler): 
#      scheduler.enter(5, 1, loop, (scheduler,))
#      print(f"UV Index: {uv_index.value}", f"Exposure Risk: {uv_index.get_exposure_risk()}")
    
# my_scheduler = sched.scheduler(time.time, time.sleep)
# my_scheduler.enter(60, 1, loop, (my_scheduler,))
# my_scheduler.run()

# with open('prueba1.csv', 'w', newline='') as csvfile:
#       spamwriter = csv.writer(csvfile, delimiter = ' ', quotechar = '|', quoting=csv.QUOTE_MINIMAL)
#       spamwriter.writerow([f'UV Index:{uv_index.value}', f'Exposure Risk: {uv_index.get_exposure_risk()}'])

# file = open('prueba1.csv', 'a')

# file.write('medicion,uv\n')
medicion = 0


while True:
 file = open('prueba1.csv', 'a')
 medicion += 1

 if medicion == 1:
    print("Iteracion,UV")
    file.write('Iteracion,UV\n')

 file.write(f'{medicion},{uv_index.value}\n')
 print(f'{medicion},{uv_index.value}\n')
 time.sleep(6)

 file.close()
