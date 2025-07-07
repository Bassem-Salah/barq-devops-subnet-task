(1)which subnet has the most hosts?

-255.255.252.0

(2)Are there any overlapping subnets? If yes, which ones?

-Subnet Masks that involved in overlaps and their peers :
 [255.255.255.0] , [255.255.252.0] , [255.255.254.0]

-192.168.100.0/22 → overlaps with:
    - 192.168.2.0/24
    - 192.168.3.0/24
    - 192.168.4.0/24
    - 192.168.10.0/24
    - 192.168.20.0/22

192.168.20.0/22 → overlaps with:
    - 192.168.10.0/24
    - 192.168.100.0/22

192.168.2.0/24 → overlaps with:
    - 192.168.100.0/22

192.168.3.0/24 → overlaps with:
    - 192.168.100.0/22

192.168.4.0/24 → overlaps with:
    - 192.168.100.0/22

192.168.10.0/24 → overlaps with:
    - 192.168.100.0/22
    - 192.168.20.0/22

172.16.0.0/23 → overlaps with:
    - 172.16.8.0/23
    - 172.16.15.0/23
    - 172.16.40.0/24
    - 172.16.50.0/22
    - 172.16.60.0/22

172.16.50.0/22 → overlaps with:
    - 172.16.0.0/23
    - 172.16.60.0/22

172.16.60.0/22 → overlaps with:
    - 172.16.0.0/23
    - 172.16.50.0/22

172.16.8.0/23 → overlaps with:
    - 172.16.0.0/23

172.16.15.0/23 → overlaps with:
    - 172.16.0.0/23

172.16.40.0/24 → overlaps with:
    - 172.16.0.0/23

10.0.0.0/23 → overlaps with:
    - 10.0.3.0/24
    - 10.2.0.0/22

10.2.0.0/22 → overlaps with:
    - 10.0.0.0/23
    - 10.3.0.0/22

10.3.0.0/22 → overlaps with:
    - 10.2.0.0/22
    - 10.4.3.0/24
    - 10.15.4.0/22

10.4.3.0/24 → overlaps with:
    - 10.3.0.0/22
    - 10.15.4.0/22

10.15.4.0/22 → overlaps with:
    - 10.3.0.0/22
    - 10.4.3.0/24
    - 10.50.2.0/24

10.50.2.0/24 → overlaps with:
    - 10.15.4.0/22

(3)what is the smallest and largest subnet in terms of address space?
 -smallest : 255.255.255.0 (254 usable hosts)
 -largest : 255.255.252.0 (1022 usable hosts)

(4)Suggest a subnetting strategy that could reduce wasted IPs in this network
   Use Smaller CIDR Blocks through Reduing /24 down to more appropriate sizes based on actual host needs
   OR
   Consider CIDR Aggregation in Routing: Once smaller subnets are in place, you can group them logically into supernets for easier routing
