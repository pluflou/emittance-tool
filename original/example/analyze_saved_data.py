import matplotlib.pyplot as plt
import sys
if '..' not in sys.path:
    sys.path.append('..')

import h5_storage
import beamdynamics
import plot_results

plt.close('all')

data = h5_storage.loadH5Recursive('./20210531_180547_EmittanceTool.h5')
meta_data = beamdynamics.analyzePyscanResult(data)
data['Meta_data'] = meta_data
plot_results.plot_all(data)

plt.show()

