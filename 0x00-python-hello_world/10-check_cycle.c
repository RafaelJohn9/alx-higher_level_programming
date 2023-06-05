#include "lists.h"

/**
 * check_cycle-checking for cycles
 * list:struct
 * Return:boolean
 */
int check_cycle(listint_t *list)
{
	listint_t *tortoise;
	listint_t *hare;

	while (list)
	{
		if (list->next)
		{
			tortoise = list->next;
		}
		else
		{
			return (0);
		}
		if (list->next->next)
		{
			hare = list->next->next;
		}
		else
		{
			return (0);
		}
		if (hare == tortoise)
		{
			return(1);
		}
		list = list->next;
	}
	return (0);
}
