import unittest


# Import the solution function
def count_ways(n):
    """
    Count the number of ways to sum up to n using positive integers in descending order.
    """
    dp = [1] + [0] * n
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            dp[j] += dp[j - i]
    return dp[n]


def process_input(input_data):
    # Parse all numbers from inputData
    all_numbers = [int(x) for x in input_data.split()]

    # First number is the count of test cases
    t = all_numbers[0]

    # The next t numbers are the test cases
    results = []
    for i in range(1, min(t + 1, len(all_numbers))):
        n = all_numbers[i]
        results.append(str(count_ways(n)))

    return "\n".join(results)


class TestPartitionCounting(unittest.TestCase):
    def test_sample_from_prompt(self):
        """Test the sample input/output given in the prompt"""
        input_data = "7 1 2 3 4 5 7"
        expected_output = "1\n2\n3\n5\n7\n15"
        self.assertEqual(process_input(input_data), expected_output)

    def test_single_case(self):
        """Test single case example from the prompt"""
        input_data = "1 5"
        expected_output = "7"
        self.assertEqual(process_input(input_data), expected_output)

    def test_edge_cases(self):
        """Test edge cases"""
        # n = 1
        self.assertEqual(process_input("1 1"), "1")

        # n = 200 (max value mentioned in the problem)
        self.assertEqual(process_input("1 200"), str(count_ways(200)))

    def test_additional_cases(self):
        """Test additional cases"""
        # Medium sized numbers
        input_data = "5 6 10 15 20 25"
        expected = [count_ways(n) for n in [6, 10, 15, 20, 25]]
        expected_output = "\n".join(map(str, expected))
        self.assertEqual(process_input(input_data), expected_output)

        # Prime numbers
        input_data = "4 11 13 17 19"
        expected = [count_ways(n) for n in [11, 13, 17, 19]]
        expected_output = "\n".join(map(str, expected))
        self.assertEqual(process_input(input_data), expected_output)

    def test_sequential_numbers(self):
        """Test a sequence of consecutive numbers"""
        input_data = "10 1 2 3 4 5 6 7 8 9 10"
        expected = [count_ways(n) for n in range(1, 11)]
        expected_output = "\n".join(map(str, expected))
        self.assertEqual(process_input(input_data), expected_output)


def main():
    # Simple test function to run without unittest
    test_cases = [
        # Cases from the prompt
        {"input": "1 5", "expected": "7", "description": "Example from prompt"},
        {"input": "7 1 2 3 4 5 7", "expected": "1\n2\n3\n5\n7\n15", "description": "Sample from prompt"},
        # Edge cases
        {"input": "1 1", "expected": "1", "description": "Smallest input"},
        {"input": "1 200", "expected": str(count_ways(200)), "description": "Maximum input"},
        # Additional cases
        {
            "input": "3 6 10 15",
            "expected": "\n".join([str(count_ways(n)) for n in [6, 10, 15]]),
            "description": "Medium values",
        },
        {
            "input": "4 11 13 17 19",
            "expected": "\n".join([str(count_ways(n)) for n in [11, 13, 17, 19]]),
            "description": "Prime numbers",
        },
        {
            "input": "2 100 150",
            "expected": "\n".join([str(count_ways(n)) for n in [100, 150]]),
            "description": "Large values",
        },
    ]

    print("Running test cases:")
    print("-" * 50)

    for i, test in enumerate(test_cases):
        input_data = test["input"]
        expected = test["expected"]
        actual = process_input(input_data)

        result = "PASS" if actual == expected else "FAIL"

        print(f"Test {i + 1}: {test['description']} - {result}")
        print(f"Input: {input_data}")
        if result == "FAIL":
            print(f"Expected: {expected}")
            print(f"Actual:   {actual}")
        print("-" * 50)


if __name__ == "__main__":
    # Run the simple test function
    main()

    # Or run the unittest tests
    # unittest.main()
