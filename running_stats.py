"""
Running 10k and finding out how quick that is on average
"""


def avg_run_time():
    """
    Take times of runs and output average
    """

    number_of_runs = 0
    total_run_time = 0

    while True:

        one_run = input("Enter the time it took you to run 10km: ")

        if not one_run:
            break

        number_of_runs += 1
        total_run_time += float(one_run)

    print(f"Average of {total_run_time/number_of_runs:.2f}"
          "over {number_of_runs}.")


if __name__ == "__main__":
    avg_run_time()
