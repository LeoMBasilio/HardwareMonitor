from Controllers.cpuController import CPUController
from Controllers.userController import USERCONTROLLER
from Controllers.memoryController import MEMORYController
from Controllers.diskController import DISKController
from Controllers.networkController import NETWORKCONTROLLER

from tkinter import *
from tkinter import ttk

cpu = CPUController()
user = USERCONTROLLER()
memory = MEMORYController()
disk = DISKController()
network = NETWORKCONTROLLER()

root = Tk()
root.title("Hardware Monitor")
root.geometry("1080x1920")

frm = ttk.Frame(root, padding=10)
frm.grid()

ttk.Label(frm, text="User").grid(column=4, row=0)
ttk.Label(frm, text=f"User: {user.getUser().get_name()}").grid(column=4, row=1)
ttk.Label(frm, text=f"Host: { 'Local ' if user.getUser().get_host() == None else user.getUser().get_host()}").grid(column=4, row=2)
ttk.Label(frm, text=f"PID: {'' if user.getUser().get_pid() == None else user.getUser().get_pid()}").grid(column=4, row=3)
ttk.Label(frm, text=f"Started: {user.getUser().get_started()}").grid(column=4, row=4)

ttk.Label(frm, text="CPU").grid(column=0, row=0)
ttk.Label(frm, text=f"Percent: {cpu.get_cpu().get_percent()}").grid(column=0, row=3)
ttk.Label(frm, text=f"Core: {cpu.get_cpu().get_core()}").grid(column=0, row=2)
ttk.Label(frm, text=f"Frequency: {cpu.get_cpu().get_frequency()}").grid(column=0, row=1)

ttk.Label(frm, text="Memory").grid(column=1, row=0)
ttk.Label(frm, text=f"Percent: {memory.getMemory().get_percent()}").grid(column=1, row=3)
ttk.Label(frm, text=f"Total: {memory.getMemory().get_total()}").grid(column=1, row=2)
ttk.Label(frm, text=f"Used: {memory.getMemory().get_used()}").grid(column=1, row=1)

ttk.Label(frm, text="Disk").grid(column=2, row=0)
ttk.Label(frm, text=f"Percent: {disk.getDisk().get_percent()}").grid(column=2, row=3)
ttk.Label(frm, text=f"Total: {disk.getDisk().get_total()}").grid(column=2, row=2)
ttk.Label(frm, text=f"Used: {disk.getDisk().get_used()}").grid(column=2, row=1)

ttk.Label(frm, text="Network").grid(column=3, row=0)
ttk.Label(frm, text=f"Send: {network.getNetwork().get_send()}").grid(column=3, row=3)
ttk.Label(frm, text=f"Recv: {network.getNetwork().get_recv()}").grid(column=3, row=2)
ttk.Label(frm, text=f"Speed: {network.getNetwork().get_speed()}").grid(column=3, row=1)
ttk.Label(frm, text=f"Packets loss: {network.getNetwork().get_packets_loss()}%").grid(column=3, row=4)



root.mainloop()