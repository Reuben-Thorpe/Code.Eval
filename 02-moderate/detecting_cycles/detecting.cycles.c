# include <stdlib.h>
# include <stdio.h>
# include <time.h>

void cycle_brent (int seq[], int x0, int *lam, int *mu );




int main(int argc, const char* argv[1]) {
  int seq[] = {3, 4, 8, 0, 11, 9, 7, 2, 5, 6, 10, 1, 49, 49, 49, 49};
  int lam, mu;

  cycle_brent(seq, 0, &lam, &mu);

  printf("lam: %d, mu: %d\n", lam, mu);

};
















/******************************************************************************/

void cycle_brent ( int seq[], int x0, int *lam, int *mu )

/******************************************************************************/
/*
  Purpose:

    CYCLE_BRENT finds a cycle in an iterated mapping using Brent's method.

  Discussion:

    Suppose we a repeatedly apply a function f(), starting with the argument
    x0, then f(x0), f(f(x0)) and so on.  Suppose that the range of f is finite.
    Then eventually the iteration must reach a cycle.  Once the cycle is reached,
    succeeding values stay within that cycle.

    Starting at x0, there is a "nearest element" of the cycle, which is
    reached after MU applications of f.

    Once the cycle is entered, the cycle has a length LAM, which is the number
    of steps required to first return to a given value.

    This function uses Brent's method to determine the values of MU and LAM,
    given F and X0.

  Licensing:

    This code is distributed under the GNU LGPL license.

  Modified:

    18 June 2012

  Author:

    John Burkardt

  Reference:

    Richard Brent,
    An improved Monte Carlo factorization algorithm,
    BIT,
    Volume 20, Number 2, 1980, pages 176-184.

  Parameters:

    Input, int F ( int i ), the name of the function 
    to be analyzed.

    Input, int X0, the starting point.

    Output, int *LAM, the length of the cycle.

    Output, int *MU, the index in the sequence starting
    at X0, of the first appearance of an element of the cycle.
*/
{
  int hare;
  int i;
  int power;
  int tortoise;

  power = 1;
  *lam = 1;
  tortoise = x0;
  hare = seq[x0];

  while ( tortoise != hare )
  {
    if ( power == *lam )
    {
      tortoise = hare;
      power = power * 2;
      *lam = 0;
    }
    hare = seq[hare];
    *lam = *lam + 1;
  }
 
  *mu = 0;
  tortoise = x0;
  hare = x0;

  for ( i = 0; i < *lam; i++ )
  {
    hare = seq[hare];
  }

  while ( tortoise != hare )
  {
    tortoise = seq[tortoise];
    hare = seq[hare];
    *mu = *mu + 1;
  }

  return;
}
