import sys

script, input_encoding, error = sys.argv

def main(language_file, encoding, errors):
    line = language_file.readline()

    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)


def print_line(line, encoding, errors):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    print(raw_bytes, "<===>", cooked_string)


languages = open("ex23_languages.txt", encoding="utf-8")

main(languages, input_encoding, error)

print("Let's practice everything.")
print('You\'d need to know \'bout escaptes with \\ that do:')
print('\n newlines and \t tabs.')

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern\n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print("-----------")
print(poem)
print("-----------")

five = 10 - 2 + 3 - 6
print(f"This should be five: {five}")

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates   #inside the function the variable is temporary
                                       #once returned, it can be assigned to a variable for later
                                       #new variable names (e.g."x, y, z, and start_point") can
                                       #hold the return values
start_point = 10000
x, y, z = secret_formula(start_point)

# remember that this is another way to format a string
print("With a starting point of: {}".format(start_point))
# it's just like with an f"" string
print(f"We'd have {x} beans, {y} jars, and {z} crates.")

start_point = start_point / 10

print("We can also do that this way:")
formula = secret_formula(start_point)
# this is an easy way to apply a list to a format string
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))
