import json
import os
import subprocess


def verify_area(nodeID,networkID, areanum):
    #Use subprocess module to run shell commands from python
    output = subprocess.Popen('docker exec {} vtysh -c "show ip interface json" '.format(nodeID),stdout=subprocess.PIPE, shell=True)
    #Pipelining vtysh commands with proper quotes need to be handled here
    (out, err) = output.communicate()

    out_dict= json.loads(out)

    for entry in out_dict['interfaces']:
        anum=entry["area"].strip(".")[-1]
        netid=entry["ipAddress"].strip(".")[:3]
        if netid == networkID.strip(".")[:3]:
            if anum == areanum:
                return True
            else:
                return False
        else:
            return False

numberOfCommands = []  #List contains node-network-area as element

f = open("./ospf_configuration_file.txt", "r")
lines = f.readlines()

for line in  lines:
    #['P1', 'eth101', '(192.168.8.1/24)', '---', 'H1', 'eth71', '(192.168.8.2/24)', '--Area', '0\n']
    #Above line contains two command elements. First half on P1, second half on H1

    ##### Append first half in list of commands #####
    element = []   #list of strings containing node, network and area
    element.append(line.split(',')[0])
    element.append(line.split(',')[2].strip('(').strip(')'))
    element.append(line.split(',')[-1].strip('\n'))
    numberOfCommands.append(element)
    ##### Append second half in list of commands #####
    #<Insert your code here>
    element=[]
    element.append(x[4])
    element.append(line.split(',')[6].strip('(').strip(')'))
    element.append(line.split(',')[-1].strip('\n'))
    numberOfCommands.append(element)
    for command in numberOfCommands:
    val= False
    val= verify_area(command[0],command[1],command[2])
    if val== True:
        print("correct config for host, network", command[0], command[1])
    else:
        print("incorrect")
                             