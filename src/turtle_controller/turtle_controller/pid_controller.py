import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math

class PIDController(Node):
    def __init__(self):
            super().__init__('pid_controller')
                    self.publisher = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
                            self.subscriber = self.create_subscription(Pose, '/turtle1/pose', self.pose_callback, 10)
                                    self.kp_linear = 1.5
                                            self.kp_angular = 4.0
                                                    self.target_x = 8.0
                                                            self.target_y = 8.0
                                                                    self.get_logger().info('PID Controller started. Target: x=%.1f y=%.1f' % (self.target_x, self.target_y))

                                                                        def pose_callback(self, pose):
                                                                                dx = self.target_x - pose.x
                                                                                        dy = self.target_y - pose.y
                                                                                                distance = math.sqrt(dx**2 + dy**2)
                                                                                                        angle_to_target = math.atan2(dy, dx)
                                                                                                                angle_error = angle_to_target - pose.theta
                                                                                                                        while angle_error > math.pi: angle_error -= 2*math.pi
                                                                                                                                while angle_error < -math.pi: angle_error += 2*math.pi
                                                                                                                                        cmd = Twist()
                                                                                                                                                if distance > 0.1:
                                                                                                                                                            cmd.linear.x = self.kp_linear * distance
                                                                                                                                                                        cmd.angular.z = self.kp_angular * angle_error
                                                                                                                                                                                else:
                                                                                                                                                                                            self.get_logger().info('Target reached!')
                                                                                                                                                                                                        cmd.linear.x = 0.0
                                                                                                                                                                                                                    cmd.angular.z = 0.0
                                                                                                                                                                                                                            self.publisher.publish(cmd)

                                                                                                                                                                                                                            def main(args=None):
                                                                                                                                                                                                                                rclpy.init(args=args)
                                                                                                                                                                                                                                    node = PIDController()
                                                                                                                                                                                                                                        rclpy.spin(node)
                                                                                                                                                                                                                                            rclpy.shutdown()

                                                                                                                                                                                                                                            if __name__ == '__main__':
                                                                                                                                                                                                                                                main()