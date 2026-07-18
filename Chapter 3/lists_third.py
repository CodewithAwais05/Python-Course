# Program to demonstrate slicing and copying lists

colors = ["red", "green", "blue", "yellow", "black"]

print("Original list:", colors)
print("First three colors:", colors[0:3])
print("Last two colors:", colors[-2:])

copied_colors = colors[:]
print("Copied list:", copied_colors)
