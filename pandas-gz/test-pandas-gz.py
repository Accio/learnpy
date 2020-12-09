import pandas as pd

a = pd.read_csv("test.tsv", sep="\t")
b = pd.read_csv("test.tsv.gz", sep="\t")

pd.testing.assert_frame_equal(a, b)


