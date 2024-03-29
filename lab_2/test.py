import math
import logging
import mpmath
import json

PI = [0.2148, 0.3672, 0.2305, 0.1875]
M_BLOCK = 8

logging.basicConfig(level=logging.DEBUG, filename="result_test.txt", filemode='w')


def frequency_test(bits: str) -> float:
    """
       Perform the frequency test on the given binary sequence.

       Args:
           bits (str): The binary sequence to perform the test on.

       Returns:
           float: The p-value of the test.
   """
    try:
        sum = 0
        length = len(bits)
        switch_case = {"0": -1, "1": 1}
        for bit in bits:
            sum += switch_case[bit]
        return math.erfc((math.fabs(sum) / math.sqrt(length)) / math.sqrt(2))
    except ZeroDivisionError as ex:
        logging.error("Division be zero.")
    except Exception as ex:
        logging.error(f"An error occurred in frequency_test: {ex}")


def test_for_runs(bits : str) -> float:
    """
    Perform the test for runs on the given binary sequence.

    Args:
        bits (str): The binary sequence to perform the test on.

    Returns:
        float: The p-value of the test.
    """
    try:
        length = len(bits)
        p = bits.count("1") / length
        if math.fabs(p - 0.5) < 2 / math.sqrt(length):
            v_n = 0
            for i in range(0, length - 1):
                if bits[i] != bits[i + 1]:
                    v_n += 1
            p_value = (math.erfc(math.fabs(v_n - 2 * length * p * (1 - p)) / (2 * math.sqrt(2 * length) * p * (1 - p))))
            return p_value
        return 0
    except ZeroDivisionError as ex:
        logging.error("Division be zero.")
    except Exception as ex:
        logging.error(f"An error occurred in test_for_runs: {ex}")


def longest_run_of_ones_test(bits : str) -> float:
    """
    Perform the Longest Run of Ones in a Block Test on the given binary sequence.

    Args:
        bits (str): The binary sequence to perform the test on.

    Returns:
        float: The p-value of the test.
    """
    try:
        length = len(bits)
        v = {1: 0, 2: 0, 3: 0, 4: 0}
        for i in range(0, length, M_BLOCK):
            len_one, max_len_one = 0 ,0
            for bit in bits[i: i + M_BLOCK]:
                len_one = len_one + 1 if bit == "1" else 0
                max_len_one = max(max_len_one, len_one)
            match max_len_one:
                case 0 | 1:
                    v[1] += 1
                case 2:
                    v[2] += 1
                case 3:
                    v[3] += 1
                case _:
                    v[4] += 1
        x_x = sum((v[i + 1] - 16 * PI[i]) ** 2 / (16 * PI[i]) for i in range(4))
        return mpmath.gammainc(3 / 2, x_x / 2)
    except Exception as ex:
        logging.error(f"An error occurred in longest_run_of_ones_test: {ex}")


if __name__ =="__main__":
    try:
        with open("sequence.json", "r") as f:
            data = json.load(f)

        logging.info("Result from frequency_test for C++: %s", frequency_test(data["cpp_sequence"]))
        logging.info("Result from test_for_runs for C++: %s", test_for_runs(data["cpp_sequence"]))
        logging.info("Result from longest_run_of_ones_test C++: %s", longest_run_of_ones_test(data["cpp_sequence"]))

        logging.info("Result from frequency_test for Java: %s", frequency_test(data["java_sequence"]))
        logging.info("Result from test_for_runs for Java: %s", test_for_runs(data["java_sequence"]))
        logging.info("Result from longest_run_of_ones_test for Java: %s", longest_run_of_ones_test(data["java_sequence"]))
    except Exception as ex:
        logging.error(f"An error occurred in main: {ex}")