# Bignum arithmetic experiments

## Description

This repository is made for experiments implemented in Python, comparing floating-point algorithms and algorithms with bignum arithmetic that can mitigate floating-point error.

Two problems were chosen for the experiments: solving a system of linear equations by the Gauss method and solving the Cauchy problem of a differential equation by approximating the derivative on the partition of a segment. Each of the tasks was tested for the feasibility of using bignum arithmetic.

## Results

The results showed that bignum arithmetic is indeed able to mitigate floating point error if accuracy is much more important than performance. Performance can be improved by optimizing Python bignum arithmetic.
