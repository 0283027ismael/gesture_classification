import os
import gc

import numpy as np
import matplotlib.pyplot as plt
import wfdb

data_folder = 'your_path'

for session in range(1, 4):
 for subject in range(1, 44):
     for gesture in range(1, 18):
         for trial in range(1, 8):
             record_name = f"session{session}_participant{subject}_gesture{gesture}_trial{trial}"
             record_path = os.path.join(data_folder, f"Session{session}/session{session}_participant{subject}/{record_name}")
             signal, fields = wfdb.rdsamp(record_path, sampto=1000)

             plt.figure(figsize=(5, 5), tight_layout=True)

             for channel in range(signal.shape[1]):
                 plt.plot(signal[:, channel])

             # Adjust axes limits to remove extra space,
             plt.xlim(0, signal.shape[0])  # Make sure to set limits based on your signal length,
             plt.ylim(np.min(signal), np.max(signal))  # Set Y limits according to your data,

             # Remove the axes,
             plt.axis('off')

             plt.savefig(f'{data_folder}/output_images_3/{record_name}.jpg', bbox_inches='tight', pad_inches=0, format='jpeg')

             plt.close()

