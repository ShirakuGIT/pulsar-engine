# include <stdio.h>
# include <stdlib.h>
# include <stdint.h>

int main() {
	printf("%s", "Printing numbers upto 100\n");

	for (int i=1; i<101; ++i)
	{
		printf("%d\n", i);
	}	

	return 0;

}