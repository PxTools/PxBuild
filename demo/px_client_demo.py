# These 3 lines are here since we are using files in the same repo, not from a package.
import sys

my = sys.path[0].replace("\\demo", "\\")
sys.path.insert(1, my)

# Create empty model:
import pxbuild

model = pxbuild.PXFileModel()

# Add stuff to model

model.axis_version.set("2023")

# model.

# model.title.set(titleText="Yxi Kaksi", lang="fi")
# model.title.set(value="Nice table", lang="en")

model.title.set("Yxi Kaksi", "fi")
model.title.set("Fin tabell")
model.tableid.set("123132")
model.decimals.set(15)
model.languages.set(["no", "en", "fi"])
model.language.set("no")


model.codes.set(codes=["c1", "c2", "c3"], variable="var_c")
model.codes.set(codes=["c1", "c2", "c4"], variable="var_d")

model.codes.set(codes=["c1", "c2", "c3"], variable="var_c", lang="en")

model.precision.set(4, "var_c", "c2", "en")

model.partitioned.set(["part11", "2"], "var_D", "en")
model.partitioned.set(["part21", "2"], "var_D", "en")

model.timeval.set("A1", ["2020", "2021"], "tid")
model.aggregallowed.set(True)
model.stockfa.set("A", None, "no")


# data:


datastring = """
"......." "......." "......." "......."
"......." "......." "......." "......."
1.2 0.9 34161.0 29982.0
"......." "......." "......." "......."
"......." "......." "......." "......."
0.8 1.7 12532.0 13361.0
"......." "......." "......." "......."
1.5 1.8 11632.0 11767.0
"..." "..." "..." "..."
0.1 0.1 13901.0 8916.0
"..." "..." "..." "..."
0.1 "..." 7779.0 "..."
2.6 4.4 18678.0 25241.0
"""


model.data.set(datastring.split())
print("\n\n--------   model before cleaner:")
print(model)


pxbuild.apply_default_language(model)
print("\n\n-------- model after cleaner:")
print(model)


# temp = ValidatePx(a)
# if ! temp.is_all_valid()
#   print (for x in getReport ; print x.problems )
