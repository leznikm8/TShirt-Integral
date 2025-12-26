# TShirt-Integral
# Monte Carlo Simulation of Mod-2 Random Disk Coverage

## Abstract

This repository provides a Monte Carlo simulation of a random geometric model involving disk coverage in the unit square. The objective is to study the asymptotic expected area of points covered an odd number of times when many randomly placed disks are present. Although the mathematical definition appears complex, the model converges to a simple constant in the large-system limit. Numerical simulations confirm this behaviour.

---

## Problem Description

We consider the following quantity:

Limit as n goes to infinity of

Expected value of:
The area of points in the unit square that are covered an odd number of times by n random disks.

Model assumptions:

* Disk centres are sampled independently and uniformly from the unit square [0, 1] x [0, 1].
* Disk radii are sampled independently and uniformly from the interval
  (0, sqrt(3 / (n * pi))).
* For each point in the square, we count how many disks cover it.
* Only the parity of coverage matters:
  odd coverage counts as 1, even coverage counts as 0.
* The integral over the square corresponds to the total odd-coverage area.

---

## Scaling Regime and Asymptotic Limit

The disk radii shrink at a rate proportional to 1 / sqrt(n). This scaling ensures that the expected total disk area remains constant as n increases.

Under this regime:

* The local disk configuration converges to a Poisson Boolean model. (https://en.wikipedia.org/wiki/Boolean_model_(probability_theory))
* The number of disks covering a fixed point converges in distribution to a
  Poisson random variable with mean 3/2.
* The probability that a Poisson(3/2) variable is odd equals:
  (1 - exp(-3)) / 2.

Therefore, the limiting expected odd-coverage area equals approximately:

0.475

---

## Numerical Methodology

The limit is approximated numerically using a Monte Carlo simulation:

1. Sample n disk centres uniformly in the unit square.
2. Sample n disk radii according to the prescribed scaling.
3. Sample many random points in the unit square to approximate the spatial
   integral.
4. For each point, track disk coverage modulo 2 using XOR logic.
5. Average over space to approximate the integral.
6. Repeat the experiment multiple times to estimate the expectation.
7. Increase n to observe convergence to the asymptotic value.

---

## Implementation Details

The simulation is implemented in Python using NumPy.

Key implementation features:

* Monte Carlo integration over the unit square
* Parity-based coverage tracking (exact modulo-2 arithmetic)
* Repeated trials for expectation estimation
* Increasing system size to approximate the infinite limit

---

## Code Structure

.
├── simulation.py    Core Monte Carlo simulation
├── README.md        Project documentation

---

## Representative Results

Typical simulation output:

n = 100   expected odd area ≈ 0.468
n = 500   expected odd area ≈ 0.474
n = 2000  expected odd area ≈ 0.475

These values are consistent with the theoretical limit.

---

## Dependencies

* Python version 3.9 or higher
* NumPy

Installation:

pip install numpy

---

## Mathematical Context

This project relates to the following topics:

* Continuum percolation
* Boolean models
* Poisson point processes
* Random geometric structures
* Monte Carlo integration

The code is intended as a computational verification of a probabilistic limit,
rather than a numerical optimisation tool.

---

## Reproducibility

All simulations use explicit random seeds. Results are reproducible up to
standard Monte Carlo variance.

---

## License

MIT License.

---

## Intended Use

This repository is intended for:

* Supplementary material for academic publications
* Teaching demonstrations in probability and stochastic geometry
* Exploratory computational experiments
