import rospy
from std_msgs.msg import String


rospy.init_node('no1')
wait = 'Esperando soma'

def somaCallBack(msg_soma):
    global wait
    wait = msg_soma.data

def timerCallBack(event):
    print(wait)
    msg = String()
    msg.data = '2017003253'
    pub.publish(msg)


pub = rospy.Publisher('/topic1', String, queue_size=1)
timer = rospy.Timer(rospy.Duration(0.1), timerCallBack)
sub = rospy.Subscriber('/topic2', String, somaCallBack)

rospy.spin()