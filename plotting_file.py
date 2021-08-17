from matplotlib import pyplot as plt
import numpy as np

def imu_ekf_plots(filename_imu, filename_ekf, title):

    time_imu, x_imu, y_imu, z_imu, w_imu = np.loadtxt(filename_imu, 
                                                unpack=True,
                                                delimiter=",")

    time_ekf, x_ekf, y_ekf, z_ekf, w_ekf = np.loadtxt(filename_ekf, 
                                                unpack=True,
                                                delimiter=",")

    plt.title(title)
    plt.ylabel("Quaternion Values")
    plt.xlabel("Time [s]")
    plt.plot(time_imu, x_imu, '#2c03fc', label="Vectornav X Value", linestyle="solid")
    plt.plot(time_imu, y_imu, '#036ffc', label="Vectornav Y Value", linestyle="dotted")
    plt.plot(time_imu, z_imu, '#03cffc', label="Vectornav Z Value", linestyle="dashed")
    plt.plot(time_imu, w_imu, '#03f4fc', label="Vectornav W Value", linestyle="dashdot")

    plt.plot(time_ekf, x_ekf, '#FF0900', label="EKF X Value", linestyle="solid")
    plt.plot(time_ekf, y_ekf, '#FF5852', label="EKF Y Value", linestyle="dotted")
    plt.plot(time_ekf, z_ekf, '#FE9F9C', label="EKF Z Value", linestyle="dashed")
    plt.plot(time_ekf, w_ekf, '#F7D3D2', label="EKF W Value", linestyle="dashdot")
    plt.legend()
    plt.show()


imu_ekf_plots('IMU_static_no_bias_imu.csv', 'IMU_static_no_bias_ekf.csv', "Static EKF Quaternion Values Compared to Vectornav")