#include <stdio.h>

int main(void)
{
	char array[][100] = {"item1" , "item2", "item3"};
	size_t count = sizeof(array) / sizeof(array[0]), i = 0;
	
	printf("There are %zu items in array\n\n", count);
	for(; i < count; i++)
	{
		printf("Item %zu: %s\n", (i+1), array[i]);
	}

	return (0);
}
