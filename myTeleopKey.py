import rospy
from geometry_msgs.msg import Twist
from turtlesim.srv import TeleportAbsolute, TeleportRelative
import sys, select, termios, tty
import termios,sys,os
from numpy import pi
#Inicializa el nodo

rospy.init_node('turtlesim_keyboard',anonymous= True)
velPub = rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=10)

# Definir las teclas para el control
move_bindings = {
    'w': (1, 0),   # Avanzar
    's': (-1, 0),  # Retroceder
    'a': (0, 1),   # Girar en sentido antihorario
    'd': (0, -1),  # Girar en sentido horario
    ' ': (0, 0)    # Giro de 180°
}

# Función para mover la tortuga
def move_turtle(x, y, theta):
    twist = Twist()
    twist.linear.x = x
    twist.linear.y = 0
    twist.linear.z = 0
    twist.angular.x = 0
    twist.angular.y = 0
    twist.angular.z = theta
    velPub.publish(twist)

# Función principal
try:
    
    while True:
        key = None
        if select.select([sys.stdin], [], [], 0.1)[0]:
            key = sys.stdin.read(1)

        if key in move_bindings:
            x, theta = move_bindings[key]
            move_turtle(x, 0, theta)
        elif key == 'r':
            move_turtle(0, 0, 0)  # Retornar a la posición y orientación centrales
        elif key == '\x03':
            break  # Salir al presionar Ctrl + C

except Exception as e:
    print(e)

finally:
    move_turtle(0, 0, 0)  # Detener la tortuga antes de salir
    #termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
