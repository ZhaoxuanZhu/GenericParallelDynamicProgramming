# The Ohio State University
# Center for Automotive Research
# Author: Zhaoxuan Zhu (email: zhu.1083@osu.edu)
import argparse
from template.problem import Problem
from solver.parallel_dynamic_programming import ParallelDP


def main():
    problem = Problem()
    solver = ParallelDP()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='A generic parallel dynamic programming solver.')
    main()