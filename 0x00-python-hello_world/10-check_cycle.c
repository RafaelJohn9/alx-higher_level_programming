#include "lists.h"

/**
 * check_cycle-checking for cycles
 * list:struct
 * Return:boolean
 */
int check_cycle(listint_t *list)
{
	listint_t *tortoise = list;
	listint_t *hare = list;

	while (hare && hare->next)
	{
		tortoise = tortoise->next;
		hare = hare->next->next;
		if (hare == tortoise)
		{
			return 1;
		}
	}
	return 0;
}
