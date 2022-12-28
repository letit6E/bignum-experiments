[![Codacy Badge](https://app.codacy.com/project/badge/Grade/d7fb72f0e9dc464ab2b6404dac953533)](https://www.codacy.com/gh/letit6E/bignum-experiments/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=letit6E/bignum-experiments&amp;utm_campaign=Badge_Grade)
# Bignum arithmetic experiments

## Description

This repository is made for experiments implemented in Python, comparing floating-point algorithms and algorithms with bignum arithmetic that can mitigate floating-point error.

Two problems were chosen for the experiments: solving a system of linear equations by the Gauss method and solving the Cauchy problem of a differential equation by approximating the derivative on the partition of a segment. Each of the tasks was tested for the feasibility of using bignum arithmetic.

## Results

The results showed that bignum arithmetic is indeed able to mitigate floating point error if accuracy is much more important than performance. Performance can be improved by optimizing Python bignum arithmetic.
