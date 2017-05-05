# PyData London 2017
Code used in my PyData London 2017 presentation 'Journeys through JuPyteR'

We have the R, Python and Julia implementations of a simulation answer to this 538 riddler [problem](https://fivethirtyeight.com/features/can-you-deal-with-these-card-game-puzzles/)

There are also R and Julia translations of Python code in the book "Make your own neural network"

Many thanks to Tariq Rashid for writing this book (available [here](https://www.amazon.co.uk/Make-Your-Own-Neural-Network/dp/1530826608/ref=la_B01N1YH9L9_1_1?s=books&ie=UTF8&qid=1488134452&sr=1-1))

The notebooks ("part2_mnist_data_set.Rmd" and "part2_neural_network_mnist_data.Rmd") are 'word-for-word' translations of the Jupyter notebooks [here](https://github.com/makeyourownneuralnetwork/makeyourownneuralnetwork), so it may not be fully Rcentric, but hopefully it can be a little tool for people who want to see how a line in Python can be written in R. Likewise the notebooks "julia_part2_mnist_data_set.pynb" and "julia_part2_neural_network.ipynb" are the Julia equivalents.

An initial concern is that the R code is about twice as slow as Python code. Further profiling of the code shows that it is the last matrix multiplication of the `train` function that is taken up a huge period of time, roughly 80%. The code finds the outer product of two vectors; byte compilation, using C++ code or `tcrossprod` didn't quicken the code. Two main resons come to mind:

1) R numbers are float64 so will be slower than Python and Julia's float32s
2) The garbage collection done at the end of a for loop in R will slow things down.
