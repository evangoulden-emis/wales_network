import jinja2
import os
import argparse

def main():
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
    print(f"{args}")

if __name__ == "__main__":
    main()