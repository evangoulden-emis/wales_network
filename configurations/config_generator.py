from jinja2 import Environment, PackageLoader, select_autoescape, FileSystemLoader
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
        loader=FileSystemLoader("."),
        autoescape=select_autoescape(),
        trim_blocks=True,
        lstrip_blocks=True
    )


    device_list = []
    template = env.get_template(args.template)

    for device in data['devices']:
        general = device['general']
        vlans = device['vlans']
        vrf = device['vrf']
   
        device_list.append(template.render(
            general=general,
            vlans=vlans,
            vrf=vrf,
        )
    )
    with open(file=args.dest, mode='w') as f:
        for device in device_list:
            f.write(device)
            f.write("\n")
        print(f"Configuration generated and written to {args.dest}")


if __name__ == "__main__":
    main()