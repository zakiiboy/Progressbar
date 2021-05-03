from time import sleep
from progress.bar import Bar

with Bar('Progress:', fill='#', suffix='%(percent).1f%% Complete') as bar:
    for i in range(100):
        sleep(0.02)
        bar.next()
*************************************************************************************************************************************************
from tqdm import tqdm
x=1
for i in tqdm(range(0,100000)):
    for x in range(0,1000):
        x*=5
