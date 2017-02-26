# MYONN
R translations of Python code in the book "Make your own neural network"
Many thanks to Tariq Rashid for writing this book (available [here](https://www.amazon.co.uk/Make-Your-Own-Neural-Network/dp/1530826608/ref=la_B01N1YH9L9_1_1?s=books&ie=UTF8&qid=1488134452&sr=1-1))

The first pieces of code (part2_mnist_data_set.Rmd and part2_neural_network_mnist_data.Rmd) are 'word-for-word' translations of the Python code, so it may not be fully Rcentric, but hopefully it can be a little tool for people who want to see how to write a line written in Python can be written in R.

An initial concern is that the R code about twice as slow than the Python code. Further profiling of the code shows that it is the last matrix multiplication of the `train` function that is taken up a huge period of time, roughly 85%. The code finds the outer product of two vectors. Byte compilation, using C++ code or `tcrossprod` didn't quicken the code. 

Further extensions of this project will be:

1. see if we can get this single slow matrix calculation sped up (e.g. C++ code, a different linear algebra compiler)
2. make the code a bit more R focused, as see if the [tidyverse](https://blog.rstudio.org/2016/09/15/tidyverse-1-0-0/) can be utilised
3. look into rewriting the code in Julia.
