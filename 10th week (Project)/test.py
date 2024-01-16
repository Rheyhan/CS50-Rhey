
import argparse
 
parser = argparse.ArgumentParser(description="Hi! :3",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)

parser.add_argument("-s", "--search", help="what you gon search for")
parser.add_argument("-n", "--quantity", default=1, help="How many images are gonna be downloaded?")
parser.add_argument("-p", "--path", default="", help="Folder Destination, default: current directory")

args = vars(parser.parse_args())
