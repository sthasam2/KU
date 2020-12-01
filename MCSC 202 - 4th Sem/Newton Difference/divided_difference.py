"""
    Python Script for Implementation of Newton's Divided Difference INterpolation formula

    Authored By: Sambeg Shrestha and Sandesh Dahal
    Date: 28 November, 2020

    Reference: https://www.geeksforgeeks.org/newtons-divided-difference-interpolation-formula/
"""


class Newtons_Divided_Differnce:
    """
            A class used to represent a newton's divided differnce question

            Attributes
            ----------
            x : list <float>
                list of x values

            y : 2D list <float>
                list of functional values of x i.e. f(x) as well as divided differnces [x0,x1],...

            n : int
                cardinality of paired data
            value : float
                actual value to be interpolated
    """

    x = None
    y = None
    n = None
    value = None

    def __init__(self, x, y, n):
        """
            Initializes class object

            Parameters
            ----------
            self : object
            x : list <float>

            y : 2D list <float>

            n : int
        """

        self.x = x
        self.y = y
        self.n = n
        self.value = None

    def input_values(self):
        """
            Gets input (n,x,y) from the user

            Returns
            -------
            String literal 
        """
        # number of data
        n = int(input("Please enter the number of data to be inputted: "))
        cols, rows = n, n

        # data initialization
        x = [0 for i in range(n)]
        y = [[0 for i in range(cols)] for j in range(rows)]

        # data input
        print("\nInput values of x:")
        for i in range(n):
            x[i] = float(input(f'\tx value {i+1}: '))

        print("\nInput values of y:")
        for i in range(n):
            y[i][0] = float(input(f'\ty value {i+1}: '))

        # assign values to attribute
        self.n = n
        self.x = x
        self.y = y

        return "Values successfully inserted!"

    def check_input(self):
        """
            Checks whether the attributes x,y,n are inputted or not
        """
        if self.x == None:
            raise Exception("x is not inputted")
        if self.y == None:
            raise Exception("y is not inputted")
        if self.n == None:
            raise Exception("n is not inputted")

        return True

    def divided_difference_table(self):
        """
            Calculate the divided difference table from given set of n values of x and f(x) [y] and stores it in a 2d list i.e. it
            calculates `[x0,x1], [x0,x1,x2], ...`

            Returns
            -------
            String Literal
        """
        # assigning new variables for easy calculation
        n = self.n
        x = self.x
        y = self.y

        # check if data inputted of not
        if self.check_input() == True:
            # Loop through x,y and calculate divided differencecl
            for i in range(1, n):
                for j in range(n-i):
                    y[j][i] = ((y[j][i-1] - y[j+1][i-1])
                               / (x[j] - x[i + j]))

            # define self.y to new divided difference table
            self.y = y
            return "Divided difference table successfully calculated"

        return "Error occoured during divide difference table calculation"

    def display_difference_table(self):
        """
            Display the divided difference table
        """
        self.divided_difference_table()

        n = self.n
        x = self.x
        y = self.y
        print("\nDivided difference table\n.............................\n")

        # calculates upto which term divided difference and stores in a list
        header = []
        for i in range(1, n):
            header.append(f'[x0,...x{i}]')

        for i in range(self.n):
            # display the headers for the table like x, y, [x0,x1]
            if i == 0:
                print("  x     f(x)     ", end=" | ")
                for k in header:
                    print(k, end="  ")
                print("\n_______________________________________\n")
            # display values of table
            for j in range(n - i):
                if j == 0:
                    print(x[i], "     ", round(y[i][j], 4), "     ", end=" | ")
                else:
                    print(round(y[i][j], 4), "     ", end="    ")
            print("")

    def product_of_terms(self, i, value, x):
        """
            Calculates the product of terms
            i.e. for given mathematical function `f(x)= f(x0) + (x-x0)*f([x0,x1]) + (x-x0)(x-x1)*f([x0, x1, x2]) + ...`
            it calculates (x-x0), (x-x0)*(x-x1), (x-x0)*(x-x1)(x-x2) and so on

            Parameters
            ----------
            i : int
                term upto which product is to be carried out i.e. if i = 1, then (x-x0)*(x-x1) is calculated

            value : float
                value for which interpolation is to be carried out

            x : list<float>
                list of given values of x

            Returns
            -------
            float
                product of differnces for example (x-x0)*(x-x1)
        """
        pro = float(1)
        for j in range(i):
            pro = pro * (value - x[j])
        return pro

    def newton_interpolation_formula(self, value=None):
        """
            Applies the formula for Newton's Divided Difference interpolation
            i.e. `f(x)= f(x0) + (x-x0)*f([x0,x1]) + (x-x0)(x-x1)*f([x0, x1, x2]) + ...`

            Parameters
            ----------
            self: object

            value: float, optional
                    value for which interpolation is to be done to find corresponding value

            Returns
            -------
            float
                interpolated value rounded to 4 decimal places
        """
        # calculate the divived difference table
        self.divided_difference_table()

        # assigning values for easier usage
        x = self.x
        y = self.y
        n = self.n

        # input value from user
        if not value:
            value = float(input("\nEnter the value to be interpolated: "))

        self.value = value

        # initializing a new list to store value f(x0)
        sum = y[0][0]

        # executes formula `f(x)= f(x0) + (x-x0)*f([x0,x1]) + (x-x0)(x-x1)*f([x0, x1, x2]) + ...`
        for i in range(1, n):
            sum = sum + (self.product_of_terms(i, value, x) * y[0][i])

        return round(sum, 4)


# Driver code
def main():
    """
        function for executing the code
    """
    # input based driver code
    # instance = Newtons_Divided_Differnce()
    # instance.input_values()
    # instance.display_difference_table()
    # answer = instance.newton_interpolation_formula()
    # print(
    #     f'\nThe interpolated value corresponding to {instance.value} is {answer}')

    # predefined value driver code
    n = 4
    x = [300, 304, 305, 307]
    y = [[0 for i in range(n)] for j in range(n)]
    y[0][0] = 2.4771
    y[1][0] = 2.4829
    y[2][0] = 2.4843
    y[3][0] = 2.4871

    new_instance = Newtons_Divided_Differnce(x, y, n)
    new_instance.display_difference_table()
    new_answer = new_instance.newton_interpolation_formula()
    print(
        f'\nThe interpolated value corresponding to {new_instance.value} is {new_answer}')


if __name__ == '__main__':
    main()
