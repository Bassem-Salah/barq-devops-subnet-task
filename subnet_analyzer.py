import pandas as pd
import ipaddress as ip_addr
import visualize
import os


def read_filedata(filepath,col_attrib):
    try:
        if isinstance(filepath , str) and isinstance(col_attrib , str) :
            data= pd.read_excel(filepath)
            feature = []
            for index, row in data.iterrows():
                feature.append(row[col_attrib])  # Access the specific column
            return feature
    
    except FileNotFoundError:
        print(f"Error: File_Path '{filepath}' not found.")
    except KeyError:
        print(f"Error: Column '{col_attrib}' does not exist in the Excel file.")

def calcuate_cidr(ip,subnet):
    cidr = []
    for i in range(len(ip)):
        ip_with_mask = f"{ip[i]}/{subnet[i]}"       # Combine IP and subnet mask
        net = ip_addr.ip_network(ip_with_mask, strict=False)
        prfxlen=net.prefixlen                       #prefixlength ==> /sub
        cidr.append(f"{ip[i]}/{prfxlen}")
    return cidr

def calcuate_net_addr(ip,subnet):
    network_addresses = []
    for i in range(len(ip)):
        ip_with_mask = f"{ip[i]}/{subnet[i]}"
        network = ip_addr.ip_network(ip_with_mask, strict=False)
        network_addresses.append(network.network_address)
    return network_addresses

def calcuate_broadcast_addr(ip,subnet):
    broadcast_addresses = []
    for i in range(len(ip)):
        ip_with_mask = f"{ip[i]}/{subnet[i]}"
        network = ip_addr.ip_network(ip_with_mask, strict=False)
        broadcast_addresses.append(network.broadcast_address)
    return broadcast_addresses

def calcuate_usableHosts(ip,subnet):
    usable_hosts = []
    for i in range(len(ip)):
        ip_with_mask = f"{ip[i]}/{subnet[i]}"
        network = ip_addr.ip_network(ip_with_mask, strict=False)
        total_hosts = network.num_addresses
        if total_hosts > 2:
            usable_hosts.append(total_hosts-2)
        else:
            usable_hosts.append(total_hosts)  #peer_to_peer_network
    return usable_hosts

def grouping(ip,subnet):
    groups = {}
    for i, j in zip(ip,subnet):
        network = ip_addr.ip_network(f"{i}/{j}", strict=False)
        groups.setdefault(str(network), []).append(i)   #grouping by subnet
    return groups

def export_data_csv(ip,subnet,cidr,networkaddr,broadcastaddr,usablehosts):
    data_after_process = pd.DataFrame({
        'IP': ip,
        'Subnet': subnet,
        'CIDR': cidr,
        'network address' : networkaddr,
        'broadcast address' : broadcastaddr ,
        'usable hosts' : usablehosts
    })
    os.makedirs('./output', exist_ok=True)
    data_after_process.to_csv('./output/subnet_report.csv', index=False)

def menu():
    print("""
    1) Read data from file
    2) CIDR
    3) Network Address
    4) Broadcast Address
    5) Usable Hosts
    6) Group IPs by Subnet
    7) Export Data as CSV file
    8) Visualize number of Hosts per Subnet
    9) Exit
    """)

def main():
    ip = []
    subnet = []
    cidr = []
    network_addresses = []
    broadcast_addresses = []
    usable_hosts = []
    groups = {}
    while(True):
        menu()
        choice=input('Enter your Choice : ')
        match choice:
            case "1":
                ip = read_filedata('./ip_data.xlsx','IP Address')
                subnet = read_filedata('./ip_data.xlsx','Subnet Mask')
            case "2":
                cidr =calcuate_cidr(ip,subnet)
                print(f'-------------------------------------------------------------------------------\n{cidr}\n------------------------------------------------------------------------------')
            case "3":
                network_addresses = calcuate_net_addr(ip,subnet)
                print(f'-------------------------------------------------------------------------------\n{network_addresses}\n------------------------------------------------------------------------------')

            case "4":
                broadcast_addresses = calcuate_broadcast_addr(ip,subnet)
                print(f'-------------------------------------------------------------------------------\n{broadcast_addresses}\n------------------------------------------------------------------------------')

            case "5":
                usable_hosts = calcuate_usableHosts(ip,subnet)
                print(f'-------------------------------------------------------------------------------\n{usable_hosts}\n------------------------------------------------------------------------------')

            case "6":
                groups = grouping(ip,subnet)
                print(f'-------------------------------------------------------------------------------\n{groups}\n------------------------------------------------------------------------------')

            case "7":
                export_data_csv(ip,subnet,cidr,network_addresses,broadcast_addresses,usable_hosts)
            case "8":
                visualize.visual_hosts_p_subnet(subnet,usable_hosts)
            case "9":
                break
            case _:
                print("Invalid choice. Please select from 0 to 8.")    


main()


#calc of max hosts in subnet
""" maxusageinsubnet=subnet[usable_hosts.index(max(usable_hosts))]
    print(maxusageinsubnet)
"""
#overlapping
"""from itertools import combinations
ip = [
                "192.168.1.24", "10.1.5.4", "172.16.20.33", "192.168.100.7", "10.0.3.112",
                "172.16.1.200", "10.2.1.56", "192.168.2.3", "172.16.50.1", "10.10.0.5",
                "192.168.3.14", "10.20.4.6", "172.16.8.9", "10.4.3.2", "192.168.20.44",
                "172.16.40.22", "10.0.0.200", "192.168.10.1", "172.16.15.15", "10.3.3.9",
                "192.168.4.5", "10.50.2.7", "172.16.60.30", "192.168.7.8", "10.15.5.50"
            ]

            subnet = [
                "255.255.255.0", "255.255.254.0", "255.255.255.0", "255.255.252.0", "255.255.255.0",
                "255.255.254.0", "255.255.252.0", "255.255.255.0", "255.255.252.0", "255.255.254.0",
                "255.255.255.0", "255.255.252.0", "255.255.254.0", "255.255.255.0", "255.255.252.0",
                "255.255.255.0", "255.255.254.0", "255.255.255.0", "255.255.254.0", "255.255.252.0",
                "255.255.255.0", "255.255.255.0", "255.255.252.0", "255.255.254.0", "255.255.252.0"
            ]
            prfx = []
            network_add = []
            subnets = []

            for i in range(len(ip)):
                ip_with_mask = f"{ip[i]}/{subnet[i]}"
                net = ip_addr.ip_network(ip_with_mask, strict=False)
                prfx.append(net.prefixlen)
                network_add.append(net.network_address)
                subnets.append(net)

            # Check for overlaps
            for net1, net2 in combinations(subnets, 2):
                if net1.overlaps(net2):
                    print(f"Overlap: {net1} overlaps with {net2}")

"""