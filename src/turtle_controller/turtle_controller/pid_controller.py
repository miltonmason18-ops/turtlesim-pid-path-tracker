import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from turtlesim.srv import SetPen
import math

class PIDController(Node):
    def __init__(self):
            super().__init__('pid_controller')
                    
                            # Publisher to send velocity commands
                                    self.cmd_pub = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
                                            
                                                    # Subscriber to get current turtle position
                                                            self.pose_sub = self.create_subscription(Pose, '/turtle1/pose', self.pose_callback, 10)
                                                                    
                                                                            # Client to change pen color
                                                                                    self.pen_client = self.create_client(SetPen, '/turtle1/set_pen')
                                                                                            while not self.pen_client.wait_for_service(timeout_sec=1.0):
                                                                                                        self.get_logger().info('Waiting