from Controllers.cpuController import CPUController
from Controllers.memoryController import MEMORYController
from Controllers.diskController import DISKController
from Controllers.networkController import NETWORKCONTROLLER
from Controllers.userController import USERCONTROLLER

cpu = CPUController()
memory = MEMORYController()
disk = DISKController()
network = NETWORKCONTROLLER()
user = USERCONTROLLER()

print(cpu.get_cpu())
print(memory.getMemory())
print(disk.getDisk())
print(network.getNetwork())
print(user.getUser())