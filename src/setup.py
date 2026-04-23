from setuptools import setup

package_name = 'turtle_controller'

setup(
    name=package_name,
        version='0.0.0',
            packages=[package_name],
                data_files=[
                        ('share/ament_index/resource_index/packages',
                                    ['resource/' + package_name]),
                                            ('share/' + package_name, ['package.xml']),
                                                ],
                                                    install_requires=['setuptools'],
                                                        zip_safe=True,
                                                            maintainer='Milton Mason',
                                                                maintainer_email='miltonmason18@gmail.com',
                                                                    description='PID path tracking for turtlesim',
                                                                        license='MIT',
                                                                            entry_points