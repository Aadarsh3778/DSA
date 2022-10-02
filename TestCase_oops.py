class TestCase:

    def __int__(self):
        pass

    @staticmethod
    def evaluation(questions, ans):
        """

        :param questions: Provide the list of Questions.
        :param ans: Provide the Output from a Function.
        :return: it prints the evaluations.
        """
        red_colour_text = '\033[91m'
        green_colour_text = '\033[92m'
        end_ = '\033[0m'

        arr_ = questions["arr"]
        query_ = questions["query"]

        if questions["query"] == ans:
            result = f"{green_colour_text} Passed {end_}"
        else:
            result = f"{red_colour_text} Failed {end_}"

        print(f"Test Case:{result}\nInput1: {arr_}\nExpected Output: {query_}\n"
              f"Actual Output: {ans}")
        print("-"*30)

    @staticmethod
    def case(lst, query):
        """

        :param lst: Provide the list of Numbers.
        :param query: Provide  the expected Output
        :return: Case in dictionary formate
        # This function takes the list of elements and expected output and store them into dictionary.
        """
        list_case = {"arr": lst, "query": query}
        return list_case

    @staticmethod
    def list_of_cases(*args):
        """

        :param args: Provide the input of test cases taken from case function.
        :return: It returns the List of Test Cases.
        # This function takes the test cases from case function and convert them into List.
        """
        lst = []
        for i in args:
            lst.append(i)
        return lst
