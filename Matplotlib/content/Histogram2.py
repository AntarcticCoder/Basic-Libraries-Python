import numpy as np
import matplotlib.pyplot as plt
data = np.random.normal(10,2.5,5000) #random 5000ตัว ค่าเฉลี่ย10 ส่วนเบี่ยงเบน2.5
plt.hist(data, bins=30) #ความชันของกราฟ30เเบบ (default 10)
plt.show()