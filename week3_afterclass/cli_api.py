import argparse
p = argparse.ArgumentParser()
p.add_argument("--x", type=int, required=True)
p.add_argument("--y", type=int, required=True)
a = p.parse_args()
print(f"{a.x} + {a.y} = {a.x+a.y}")
