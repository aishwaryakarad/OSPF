import os
import subprocess

def set_ospf_process_on_node_interface(nodeID, networkID, areanum):
    #Use subprocess module to run shell commands from python
    cmd='docker exec {} vtysh -c "conf t " -c "route ospf" -c "network {} {}"'.format(nodeID, networkID,areanum)
    output = subprocess.Popen(cmd,stdout=subprocess.PIPE, shell=True)
    #Pipelining vtysh commands with proper quotes need to be handled here
    (out, err) = output.communicate()
    print(out)


numberOfCommands = []  #List contains node-network-area as element
element = []
f = open("./ospf_configuration_file.txt", "r")
lines = f.readlines()

for line in  lines:
    #['P1', 'eth101', '(192.168.8.1/24)', '---', 'H1', 'eth71', '(192.168.8.2/24)', '--Area', '0\n']
    #Above line contains two command elements. First half on P1, second half on H1

    ##### Append first half in list of commands #####
    x=line.split(',')
    xlen=len(x)
   #list of strings containing node, network and area
    element.append(x[0])
    element.append(x[2].strip('(').strip(')'))
    element.append(x[-1].strip('\n'))
    numberOfCommands.append(element)
    ##### Append second half in list of commands #####
    #<Insert your code here>
    element=[]
    element.append(x[4])
    element.append(line.split(',')[6].strip('(').strip(')'))
    element.append(line.split(',')[-1].strip('\n'))
    numberOfCommands.append(element)


for command in numberOfCommands:
    set_ospf_process_on_node_interface(command[0], command[1], command[2])