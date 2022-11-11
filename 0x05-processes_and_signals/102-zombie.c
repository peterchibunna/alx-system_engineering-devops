#include <stdio.h>
#include <unistd.h>

/**
 * infinite_while - creates an infinite loop
 * Return: 0 always
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - creates 5 zombie_process processes
 * Return: always 0
 */
int main(void)
{
	int i;
	pid_t zombie_process;

	for (i = 0; i < 5; i++)
	{
		zombie_process = fork();
		if (!zombie_process)
		{
			return (0);
		}
		printf("Zombie process created, PID: %d\n", zombie_process);
	}

	infinite_while();

	return (0);
}
