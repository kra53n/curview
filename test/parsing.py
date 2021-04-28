import yaml

with open("parsing.yaml") as f:
    yl = yaml.safe_load(f)
print(yl)
