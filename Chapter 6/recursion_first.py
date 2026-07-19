# recursion is defined as:  function calls itself repeatedly
# in simple wording, recursion is the dangerous version of the loop😂


#recursive function to print numbers from n to 1
def printing(n):
    if n == 0:  # basecase is compulsory, if not set, recursion becomes infinite
        return
    print(n, end = " ")
    printing(n-1)
    n -= 1

printing(5)