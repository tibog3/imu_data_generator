"""Create imu data."""

import sys


def read_args(argv):
    """
    Extract paramters from command line.

    :param argv:
    :return: parameters, dict filled with parsed option
    """
    parameters = {'1': argv[0], '2': 2}
    return parameters


def build_accel_data():
    """
    Create accelerometer data.

    :return: Accel data.
    """
    data = []
    return data


def build_magneto_data():
    """
    Create mageto data.

    :return: Magneto data.
    """
    data = []
    return data


def build_gyro_data():
    """
    Create gyro data.

    :return: Gyro data.
    """
    data = []
    return data


def main(argv=sys.argv):
    """Entry point ot generator."""
    parameters = read_args(argv)

    rotation = parameters['1']
    print(rotation)
    accel_data = build_accel_data()
    gyro_data = build_gyro_data()
    magneto_data = build_magneto_data()
    imu_data = {'accel': accel_data, 'gyro': gyro_data, 'magneto': magneto_data}
    return imu_data


if __name__ == '__main__':
    print(main(argv=sys.argv))
