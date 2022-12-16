import argparse
import time

from board_helper import (
    get_total_attack,
    convert_to_representation
)

from hill_climbing import (
    simple_hill_climbing
)
from simulated_annealing import (
    simulated_annealing
)

from modified_hc import (
    memory_based_simple_hill_climbing
)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("N", type=int, default=None)
    parser.add_argument("M", type=int, default=None)
    parser.add_argument("Q", type=int, default=None)
    parser.add_argument("K", type=int, default=None)
    parser.add_argument("tmax", type=int, default=None)
    parser.add_argument("fileName", type=str, default=None)
    parser.add_argument("methodName", type=str, default=None)
    args = parser.parse_args()
    N = args.N
    M = args.M
    Q = args.Q
    K = args.K
    tmax = args.tmax
    fileName = args.fileName
    methodName = args.methodName

    start_time = time.time()
    if methodName.lower().strip() == 'hc':
        final_board = simple_hill_climbing(N, M, Q, K, start_time, tmax)
    if methodName.lower().strip() == 'sa':
        final_board = simulated_annealing(N, M, Q, K, start_time, tmax)
    if methodName.lower().strip() == 'other':
        final_board = memory_based_simple_hill_climbing(N, M, Q, K, start_time, tmax)
    end_time = time.time()
    file = open(fileName, "w+")
    for row in final_board:
        lines = [convert_to_representation(col) for col in row]
        line = "".join(lines) + "\n"
        file.write(line)
    file.write(str(get_total_attack(final_board)) + "\n")
    file.close()

if __name__ == "__main__":
    main()
