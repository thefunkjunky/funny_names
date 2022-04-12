import argparse
import random
import yaml


def random_name(names):
  """Generates random name from names dict"""
  
  random_first = random.choice(names["first"])
  random_last = random.choice(names["last"])
  full_name = random_first + " " + random_last

  return full_name


def main():
  """Generates random funny names"""
  parser = argparse.ArgumentParser(
    description="Funny name generator")
  parser.add_argument(
    "--names_list",
    type=str,
    default="names.yaml",
    help="Location of names list. Default='names.yaml'")
  args = parser.parse_args()

  with open(args.names_list, "r") as f:
    names = yaml.load(f, Loader=yaml.Loader)

  full_name = random_name(names)

  print(full_name)


if __name__ == '__main__':
  main()
