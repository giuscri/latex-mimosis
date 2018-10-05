print("""
digraph G {
  node[label=""]
  splines=false
""")
for src in range(1, 5):
	for dst in range(1, 5):
		print(f"  s{src} -> d{dst}")
	print()
print("}")
