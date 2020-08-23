"""
All Possible Palindromic Partitions for the given string.
"""
from pprint import pprint


class PalindromicPartitions:
    """
    Prepare the partitions of given string using Dynamic Programming approach.
    """

    def __init__(self, text):
        self.text, self.length = text, len(text)
        self.palindrome_list = list()

        # Preparing a Null matrix for a given string.
        self.palindrome = list(map(lambda x: list(map(lambda y: 0, range(self.length))), range(self.length)))

    def set_diagonals(self):
        """
        Makes null matrix as unit matrix as each individual character in given string is palindrome.
        :return: self.lst1
        :rtype: list
        """
        lst1 = list()
        for i in range(0, self.length):
            self.palindrome[i][i] = 1
            lst1.append(self.text[i])

        self.palindrome_list.append(lst1)

    def partitions(self):
        """
        Partitioning the given string.
        :return:
        :rtype:
        """

        self.set_diagonals()
        for col in range(1, self.length):
            lst2 = []

            for row in range(0, col):
                is_same_char = (self.text[col].lower() == self.text[row].lower())

                if ((row == (col - 1)) and is_same_char) or ((self.palindrome[row + 1][col - 1] == 1) and is_same_char):
                    self.palindrome[row][col] = 1
                    lst2.append(self.text[row:col + 1])

            if lst2:
                self.palindrome_list.append(lst2)

        return self.palindrome


class StringPalindromicPartitions(PalindromicPartitions):
    """
    String Palindromic Partition.
    """

    def __init__(self, *args):
        super().__init__(*args)

    def print_matrix(self):
        """
        Print the result matrix.
        :return:
        :rtype:
        """
        pprint(self.palindrome)

    def print_palindromes(self):
        """
        Prints list of all palindrome exist in give string.
        :return:
        :rtype:
        """
        pprint(self.palindrome_list)

    def print_strings_with_palindromes(self):
        """
        Printing all strings with palindromes in it.
        :return:
        :rtype:
        """
        resulted_strings = self.partitions()

        print(' '.join(self.text))
        for c in range(len(resulted_strings)):
            for r in range(c + 1, len(self.text)):
                if resulted_strings[c][r]:
                    star = self.text.index(self.text[c:r + 1])
                    end = star + len(self.text[c:r + 1])
                    before, after = ' '.join(self.text[0:star]), ' '.join(self.text[end:])
                    print(before, self.text[c:r + 1], after)


if __name__ == '__main__':
    txt = str(input("Enter a string: "))
    # txt = 'BorrowOrRob'
    s_obj = StringPalindromicPartitions(txt)

    s_obj.print_strings_with_palindromes()
