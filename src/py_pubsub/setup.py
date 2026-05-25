from setuptools import find_packages, setup

package_name = 'py_pubsub'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='sachinator',
    maintainer_email='sachinator@example.com',
    description='Basic ROS 2 publisher and subscriber example',
    license='TODO',
    entry_points={
        'console_scripts': [
            'talker = py_pubsub.talker:main',
            'listener = py_pubsub.listener:main',
        ],
    },
)
