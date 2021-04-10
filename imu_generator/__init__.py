"""imu_generator module."""

from pkg_resources import DistributionNotFound, get_distribution

try:
    __version__ = get_distribution('imu-generator').version
except DistributionNotFound:
    pass
