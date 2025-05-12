from jinja2 import Environment, PackageLoader, select_autoescape
import os
import argparse
import yaml



def main():
    data = {}
    parser = argparse.ArgumentParser(
        description='''Provide a template, data and destination file which will be used to produce a base configuration template'''    
    )
    parser.add_argument('--template', '-t', type=str, help='The template used for config generation.')
    parser.add_argument('--data_file', '-df', type=str, help='The data file which hold the variable information which should be passed to the template for generation.')
    parser.add_argument('--dest', '-d', type=str, help='The destination file where template and data are combined to create a configuration.')

    args = parser.parse_args()
    if args.template is None or args.data_file is None or args.dest is None:
        print("Invalid combination of arguments passed or no args passed, exiting")
        return
    
    try:
        with open(file=args.data_file, mode='r') as f: 
            data = yaml.safe_load(f)
    except Exception as e:
        print(f"Failed to parse YAML document due to {e}")

    env = Environment(
        loader=PackageLoader("config_generator"),
        autoescape=select_autoescape()
    )


    device_list = []
    
    for device in data['devices']:
        '''General Device Information'''
        loopback = device['loopback']
        loopback_ip = device['loopback_ip']
        loopback_netmask = device['loopback_netmask']
        dxcon_description = device.get('dxcon').get('description')

        '''VLAN Information'''
        vlans = [vlan.get('vlan_id') for vlan in device['vlans']]
        vlan_names = [vlan.get('vlan_name') for vlan in device['vlans']]
        vlan_interface_ip = [vlan.get('vlan_interface_ip') for vlan in device['vlans']]
        vlan_interface_netmask = [vlan.get('vlan_interface_netmask') for vlan in device['vlans']]
        vlan_description = [vlan.get('vlan_description') for vlan in device['vlans']]


        '''VRF Information'''
        vrf_name = [vrf.get('name') for vrf in device['vrf']]
        vrf_description = [vrf.get('description') for vrf in device['vrf']]
        for vrf in device['vrf']:
            if 'bgp' in vrf.keys():
                for bgp in vrf['bgp']:
                    print(f"{bgp}")





        '''BGP Information'''



        device_list.append(template.render(
            

        )
    )
    template = env.get_template(args.template)


if __name__ == "__main__":
    main()