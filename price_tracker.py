import argparse
arg_parser = argparse.ArgumentParser(description='Price tracker options')


arg_parser.add_argument('-a','--add', type=str, help='add a product url')


args = arg_parser.parse_args()


product_url = args.add;

print("found ",product_url)
