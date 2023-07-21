Data structure and design principles of pandas
===

References:

1. [Intro to data structures of pandas](https://pandas.pydata.org/docs/user_guide/dsintro.html#dsintro)
2. [Data types of NumPy](https://numpy.org/doc/stable/user/basics.types.html)
3. [Essential basic functionality of pandas](https://pandas.pydata.org/docs/user_guide/basics.html#basics-binop)
4. [Lecture notes in scientific python](https://lectures.scientific-python.org)
5. [Mathesaurus, a thesaurus of mathematical languages](https://mathesaurus.sourceforge.net)

To learn the data structure and essential functionalities of pandas, it is helpful to be familiar with basic python data structures, especially list and
dict, as well as with `ndarray` of numpy.

## Series

`Series` is an array of objects, either explicitly or implicitly named. The names are known as the index of the series.

Key idea: Data and labels are automatically aligned. When two series are
involved in an operation, for instance summing, values are matched by the index values, and the union of the values are returned.

For users of the `numpy` package, the Series object acts similarly to a `ndarray`, and is a valid argument to most NumPy functions. For R users, `Series` is like (named) vectors in R.


`NaN` (not a number) indicates missing value, like `NA`is R.

The method `s.get("index")` is a more graceful method than `s["index"]`.

## DataFrame

DataFrame is in essence an ordered dict of `Series`. The `ìndex` of a DataFrame follows the index of the series objects, and the `columns` of a DataFrame are the column labels. So the index and the columns of a DataFrame correspond to the rownames and colnames of a data.frame in R, respectively.

We can use `pd.DataFrame()` to create a new data frame. In addition,
`pd.DataFrame.from_dict` and `pd.DataFrame.from_records` provides additional
methods to create DataFrame from dict or from `ndarray` defined in `numpy`, respectively.

Since `DataFrame` is an ordered dict of `Series`, so subsetting or creating a column follows the same syntax as `dict`, while popping and insertion of columns follow the same syntax as `list`.

In order to select a row by index (label), use `df.loc[label]`; to select a row with index, use `df.iloc[int]`. While a slicing of length 1 with `df[int:(int+1)]` will do the same, it reads strange. Note that `df[int]` will not work, because this collides with the syntax of getting a column.

Data alignment between DataFrame objects align both the columns and the index.

When a Series is subtracted from a DataFrame, the default behavior is to align the series index on the DataFrame columns, therefore broadcasting row-wise.

If a column name is a valid variable name of Python, the column can be assessed
with either `df["col"]` or `df.col``.

Todo: essential basic functionality, https://pandas.pydata.org/docs/user_guide/basics.html
