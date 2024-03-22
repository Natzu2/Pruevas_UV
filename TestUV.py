from pyowm import OWM
import sched, time
import csv  
import serial

owm = OWM('25e4f8c6b58ce79d30fb2f9f51c1d1a6')
uv_mgr = owm.uvindex_manager()
uv_index = uv_mgr.uvindex_around_coords(27.967115, -110.918797)

def do_something(scheduler): 
    scheduler.enter(60, 1, do_something, (scheduler,))
    print(f"UV Index: {uv_index.value}", f"Exposure Risk: {uv_index.get_exposure_risk()}")
    
my_scheduler = sched.scheduler(time.time, time.sleep)
my_scheduler.enter(60, 1, do_something, (my_scheduler,))
my_scheduler.run()

with open('ResultadosUV.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow([f'UV Index:{uv_index.value}', f'Exposure Risk: {uv_index.get_exposure_risk()}'])

