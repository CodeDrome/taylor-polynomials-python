import taylorseries
import math


def main():

    """
    Test the taylorseries module by printing sines of a range of angles using
    math.sin and then taylorseries.sine_of_radians with various degrees of the polynomial.
    """

    print("----------------------")
    print("| codedrome.com      |")
    print("| Taylor Polynomials |")
    print("----------------------\n")

    print("-----------------------------------------------------------------------------------------");
    print("| Degrees |   math.sin |   Taylor 3 |   Taylor 5 |   Taylor 7 |   Taylor 9 |  Taylor 11 |");
    print("-----------------------------------------------------------------------------------------");

    for degrees in range(0, 361, 30):

         print("| {:7.0f} | {:10.6f} | {:10.6f} | {:10.6f} | {:10.6f} | {:10.6f} | {:10.6f} |".format(
         degrees,
         math.sin(math.radians(degrees)),
         taylorseries.sine_of_radians(math.radians(degrees), 3),
         taylorseries.sine_of_radians(math.radians(degrees), 5),
         taylorseries.sine_of_radians(math.radians(degrees), 7),
         taylorseries.sine_of_radians(math.radians(degrees), 9),
         taylorseries.sine_of_radians(math.radians(degrees), 11)))

    print("-----------------------------------------------------------------------------------------");


main()
