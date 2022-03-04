#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main() {
    printf("Area of Circle Calculator v1.0\n");

    int r;

    printf("Enter radius of circle\n");

    scanf("%d", r);

    int area;

    area = 3.14*r*r;

    printf("Area of circle ");

    printf(area);
}
