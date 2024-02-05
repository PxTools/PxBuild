# The datafiles

Pxbuild accept datafiles in 2 formats parquet and semicolon-based csv. 
The csv is easier when working with test files as you can open them in notepad, and parquet is faster to process when you have more data. 
Pandas has support for both, so converting between them is easy. 

The columns is expected to look something like this:
CODED_DIM1;CODED_DIM2;CODED_DIM3;TIME;MEASURE1;MEASURE1_SYMBOL;MEASURE2;MEASURE2_SYMBOL

where MEASUREn_SYMBOL lets you specify, via datasymbolX in config, what should be shown in a datacell which has no number. 

The columnnames must be unique and without "." (dot)  and uppercase (It works with lowercase, but "_SYMBOL" must be uppercase, so.)

If a row has a value for MEASUREn then the value of MEASUREn_SYMBOL has no effect.
The valid strings for data in the *_SYMBOL columns are empty, 1 to 6 dots and -
The a row has empty MEASUREn and empty MEASUREn_SYMBOL, the value from missingCell in config is used.
An empty MEASUREn_SYMBOL column may be ommited. 
