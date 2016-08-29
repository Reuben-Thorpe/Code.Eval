// Reuben Thorpe (2016), CodeEval [File Size v1.4]
#include <stdio.h>

int main(int argc, const char * argv[]) {
    FILE *file = fopen(argv[1], "r");
    fseek(file, 0L, SEEK_END);
    printf("%i", ftell(file));
    return(0);
}
