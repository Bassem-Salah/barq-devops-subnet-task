import matplotlib.pyplot as mplt


def visual_hosts_p_subnet(subnet,usable_hosts):
    mplt.bar(subnet,usable_hosts)

    mplt.xlabel('Subnet')
    mplt.ylabel('usable hosts')
    mplt.title('usable hosts per subnets')
    
    #save chart
    mplt.savefig('./output/network_plot.png')
    # Show chart
    mplt.show()