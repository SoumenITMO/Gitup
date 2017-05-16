__author__ = 'Soumen'

import numpy as np
import pylab as pl
from pykalman import KalmanFilter

rnd = np.random.RandomState(0)

x_dat = []
y_dat = []
tmp_kal_val__ = []
counter = 0
kalman_data__ = []

with open("D3-data-file-refugee-1.csv") as csvfile:
    reader = csvfile.readlines()
    skipline = 0
    line_ = 0

    for row in reader:
        if skipline > 1 and skipline <= 38:
            x_dat.append(row.split("\t")[0])
            if line_ <= 2:
                tmp_kal_val__.append(int(row.split("\t")[8]))
                y_dat.append(int(row.split("\t")[8]))  # FOR RUSSIA
            else:
                line_ = 0
                kalman_data__.append(tmp_kal_val__)
                tmp_kal_val__ = []
            counter += 1
            line_ += 1
        skipline += 1

print(kalman_data__)


"""
n_timesteps = 10
x = np.linspace(0, 50, n_timesteps)
observations = rnd.randn(n_timesteps)
kf = KalmanFilter(transition_matrices=np.array([[y_dat[0], y_dat[1]], [y_dat[2], y_dat[3]]]))
states_pred = kf.em(observations).smooth(observations)[0]
pl.figure(figsize=(16, 6))


## --- SOLVE DATASET PROBELM --- ##
kf = KalmanFilter(transition_matrices = [[1, 1], [0, 1]], observation_matrices = [[0.1, 0.5], [-0.3, 0.0]])
steps__ = 40
x_plot_data = np.linspace(0, 50, steps__)

measurements = np.asarray([(399, 293), (403, 299), (409, 308), (416, 315), (418, 318), (420, 323), (429, 326),
                           (423, 328), (429, 334), (431, 337), (433, 342), (434, 352), (434, 349), (433, 350),
                           (431, 350), (430, 349), (428, 347), (427, 345), (425, 341), (429, 338), (431, 328),
                           (410, 313), (406, 306), (402, 299), (397, 291), (391, 294), (376, 270), (372, 272),
                           (351, 248), (336, 244), (327, 236), (307, 220)])

kf = kf.em(measurements, n_iter=5)
(filtered_state_means, filtered_state_covariances) = kf.filter(measurements)
(smoothed_state_means, smoothed_state_covariances) = kf.smooth(measurements)
print(filtered_state_means, filtered_state_covariances)
## ----------------------------- ##


obs_scatter = pl.scatter(x, observations, marker='x', color='b',
                         label='observations')
position_line = pl.plot(x, states_pred[:, 0],
                        linestyle='-', marker='o', color='r',
                        label='position est.')
velocity_line = pl.plot(x, states_pred[:, 1],
                        linestyle='-', marker='o', color='g',
                        label='velocity est.')
pl.legend(loc='lower right')
pl.xlim(xmin=0, xmax=x.max())
pl.xlabel('time')
pl.show()
"""



from pykalman import KalmanFilter
import numpy as np
import matplotlib.pyplot as plt

measurements = np.asarray([(1, 3), (5, 8), (409, 308), (416, 315), (418, 318), (420, 323), (429, 326), (423, 328),
                           (429, 334), (431, 337), (433, 342), (434, 352), (434, 349), (433, 350), (431, 350),
                           (430, 349), (428, 347), (427, 345), (425, 341), (429, 338), (431, 328), (410, 313),
                           (406, 306), (402, 299), (397, 291), (391, 294), (376, 270), (372, 272), (351, 248),
                           (336, 244), (327, 236), (307, 220)])
times = range(measurements.shape[0])

obs_mat = np.vstack([measurements, np.ones(measurements.shape)]).T[:, np.newaxis]
delta = 1e-5
trans_cov = delta / (1 - delta) * np.eye(2)
kf = KalmanFilter(transition_matrices = [[1, 1], [0, 1]], observation_matrices = [[0.1, 0.5], [-0.3, 0.0]], initial_state_mean=np.zeros(2))

"""
kf = KalmanFilter(initial_state_mean=np.zeros(2),
                  initial_state_covariance=np.ones((2, 2)),
                  transition_matrices=np.eye(2),
                  #observation_matrices = [[0.1, 0.5], [-0.3, 0.0]],
                  observation_matrices = [[1., 1.], [3., 1.]],
                  transition_covariance=trans_cov)
"""

#kf = kf.em(measurements, n_iter=10)
state_means1, state_covs1 = kf.filter(measurements)
#smoothed_state_means, smoothed_state_covariances = kf.smooth(measurements)
print(state_covs1)

pl.scatter(times,  state_covs1[:, 0], marker='*', color='b')
pl.show()


"""
plt.figure(1)
times = range(measurements.shape[0])
obs_scatter = pl.scatter(times,  measurements[:, 0], marker='*', color='b', label='Measurement of Regfuge 1')
position_line = pl.plot(times, measurements[:, 1], marker='8', color='r', label='Measurement of Regfuge 2')
velocity_line = pl.plot(times, smoothed_state_means[:, 0], linestyle='-', marker='_', color='g', label='Smoothing mean value')
#velocity_line2 = pl.plot(times, smoothed_state_means[:, 2], linestyle='-', marker='_', color='m', label='Smoothing mean value 2')
pl.legend(loc='lower right')
pl.xlabel("Time Series")
pl.ylabel("Value of Refuge")
pl.show()
"""