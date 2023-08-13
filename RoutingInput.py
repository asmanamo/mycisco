from netmiko import ConnectHandler
from getpass import getpass

username = input("enter your user name: ")
password= getpass("password please: ")

R1= {
    "ip":"192.168.242.128",
    "device_type":"cisco_ios",
    "username":username,
    "password":password
}
ssh = ConnectHandler(**R1)
print("ssh successfull with R1")

user_choice = int(input("welcome\n what you like to configure 1. static route 2. EIGRP 3. BGP"))

if user_choice==1:

    user_input = int(input("enter total number of static routes you like to add: "))
    for interface in range(0,user_input):
        nw_id = input("enter network ID ")
        mask = input("enter mask ")
        next_hop = input("enter next hop address ")

        commands = [f'ip route {nw_id} {mask} {next_hop}']

        static_conf = ssh.send_config_set(commands)
        print(static_conf)

        static_details = ssh.send_command("show runn | sec ip route")
        print(static_details)
elif user_choice==2:

    eigrp_as = (input("enter eigrp AS like to add: "))

    user_input = int(input("enter total number of network routes you like to add under EIGRP: "))

    for route in range(0,user_input):

        nw_id = input("enter network ID ")
        wmask = input("enter wild card mask ")
        commands = [f'router eigrp {eigrp_as}', f'network {nw_id} {wmask}']

        
        eigrp_conf = ssh.send_config_set(commands)
        print(eigrp_conf)

    eigrp_details = ssh.send_command("show runn | sec eigrp")
    print(eigrp_details)
elif user_choice==3:

    bgp_as = (input("enter BGP AS like to add: "))
    nw_id = input("enter network ID ")
    neighbor_ip = input("enter neighbor IP address ")
    neighbor_remote_as = input("enter neighbor remote AS ")

    commands = [f'router bgp {bgp_as}', f'network {nw_id}', f'neighbor {neighbor_ip} remote-as {neighbor_remote_as}']

    bgp_conf = ssh.send_config_set(commands)
    print(bgp_conf)

    bgp_details = ssh.send_command("show runn | sec bgp")
    print(bgp_details)
else:
    print("invalid choice you tried")    
