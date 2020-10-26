import rospy
from std_msgs.msg import String

rospy.init_node('no2')

matricula='0'

def recebe_msg(recebido):
    global matricula
    matricula = recebido.data

def timerCallBack(event):
    soma = 0
    for digit in matricula:
        soma +=int(digit)
    msg = String()
    msg.data = str(soma)
    pub.publish(msg)

pub = rospy.Publisher('/topic2', String, queue_size=1)
timer = rospy.Timer(rospy.Duration(0.1), timerCallBack)
sub = rospy.Subscriber('/topic1', String, recebe_msg)

rospy.spin()