def start_spring(**kwargs):
    result = {}
    for obj,type in kwargs.items():
        if type not in result.keys():
            result[type] = []
        result[type].append(obj)

    result = sorted(result.items(),key=lambda x:(-len(x[1]),[0],x[0]))
    output = ""
    for key,val in result:
        output += f"{key}:\n"
        for v in sorted(val):
            output += f"-{v}\n"

    return output[:-1]


example_objects = {"Magnolia": "tree",

"Swallow": "bird",

"Thrushes": "bird",

"Pear": "tree",

"Cherries": "tree",

"Shrikes": "bird",

"Butterfly": "insect"}

print(start_spring(**example_objects))




import unittest

class Tests(unittest.TestCase):
    def test(self):
        result = start_spring(
            **{"Magnolia": "tree",
                   "Swallow": "bird",
                   "Thrushes": "bird",
                   "Pear": "tree",
                   "Cherries": "tree",
                   "Shrikes": "bird",
                   "Butterfly": "insect"}


        )
        self.assertEqual(result.strip(), "bird:\n"
                                         "-Shrikes\n"
                                         "-Swallow\n"
                                         "-Thrushes\n"
                                         "tree:\n"
                                         "-Cherries\n"
                                         "-Magnolia\n"
                                         "-Pear\n"
                                         "insect:\n"
                                         "-Butterfly")

if __name__ == "__main__":
    unittest.main()