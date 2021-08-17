from matplotlib import pyplot as plt
import numpy as np

def imu_ekf_plots(filename_imu, filename_ekf, title):
    time_imu, x_imu, y_imu, z_imu, w_imu = np.loadtxt(filename_imu, 
                                                unpack=True,
                                                delimiter=",")

    time_ekf, x_ekf, y_ekf, z_ekf, w_ekf = np.loadtxt(filename_ekf, 
                                                unpack=True,
                                                delimiter=",")

    plt.title(title, fontsize=26)
    plt.ylabel("Quaternion Values", fontsize=20)
    plt.xlabel("Time [s]", fontsize=20)
    plt.plot(time_imu, x_imu, '#2c03fc', label="Vectornav X Value", linestyle="solid")
    plt.plot(time_imu, y_imu, '#2c03fc', label="Vectornav Y Value", linestyle="dotted")
    plt.plot(time_imu, z_imu, '#2c03fc', label="Vectornav Z Value", linestyle="dashed")
    plt.plot(time_imu, w_imu, '#2c03fc', label="Vectornav W Value", linestyle="dashdot")

    plt.plot(time_ekf, x_ekf, '#FF0900', label="EKF X Value", linestyle="solid")
    plt.plot(time_ekf, y_ekf, '#FF0900', label="EKF Y Value", linestyle="dotted")
    plt.plot(time_ekf, z_ekf, '#FF0900', label="EKF Z Value", linestyle="dashed")
    plt.plot(time_ekf, w_ekf, '#FF0900', label="EKF W Value", linestyle="dashdot")
    plt.legend(fontsize=16)
    plt.show()

imu_ekf_plots('lin_acc_static_imu.csv', 'lin_acc_static_ekf.csv', "Static EKF Quaternion Values Compared to Vectornav Callibrated")