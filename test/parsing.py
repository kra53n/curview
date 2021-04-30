import yaml

filename = "parsing.yaml"

with open(filename) as f:
    yl = yaml.safe_load(f)
print(yl)
