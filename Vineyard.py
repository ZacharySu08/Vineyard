"""
Author: Zachary Su, zlsu@purdue.edu
Assignment: m.n - Vineyard
Date: 09/12/2021

Description:
    The following program will be used to calculate the equation V=(R-2E)/S. This equation will be used to find the number of vines that will fit in a row.

Contributors:
    Zachary Su, zlsu@purdue.edu

My contributor(s) helped me:
    [ ] understand the assignment expectations without
        telling me how they will approach it.
    [ ] understand different ways to think about a solution
        without helping me plan my solution.
    [ ] think through the meaning of a specific error or
        bug present in my code without looking at my code.
    Note that if you helped somebody else with their code, you
    have to list that person as a contributor.

Academic Integrity Statement:
    I have not used source code obtained from any unauthorized
    source, either modified or unmodified; nor have I provided
    another student access to my code.  The project I am
    submitting is my own original work.
"""


def main():
    #asks for input of the space between vines
    S = int(input('How much space should be between the vines? '))
    #asks for input of how wide the end-post is
    E = float(input('How wide is the end-post assembly? '))
    #ask for the length of the row
    R = int(input('How long is this row? '))
    #finalizes the equation with given value
    V = str(int((R-2*E)/S))

    #print the final statement, including the solution
    print('This row has enough space for ' + V + ' vine(s)')

if __name__ == '__main__':
    main()
