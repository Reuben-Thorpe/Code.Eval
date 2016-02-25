// Reuben Thorpe (2016), CodeEval [Sum Of Primes v1.0]
#include <math.h>
#include <iostream>

using namespace std;


bool isPrime (int num) {
    // Returns true if input number is a prime
    // Credit : Grey Wolf : http://www.cplusplus.com/forum/general/1125/
    if (num <=1)
        return false;
    else if (num == 2)
        return true;
    else if (num % 2 == 0)
        return false;
    else {
        bool prime = true;
        int divisor = 3;
        double num_d = static_cast<double>(num);
        int upperLimit = static_cast<int>(sqrt(num_d) +1);
        while (divisor <= upperLimit) {
            if (num % divisor == 0)
                prime = false;
            divisor +=2;
        }
        return prime;
    }
}


int main() {
  // Search through odd integers for primes, sums the first 1000 found
  int sum = 2, num = 3, primeCount = 1;

  while (primeCount < 1000) {
    if(isPrime(num)) {
      sum += num;
      primeCount++;
    }
    num += 2;
  }
  cout << sum;
  return(0);
}
