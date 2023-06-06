#include "lists.h"
#include <stdlib.h>
/**
 * insert_node-inserts node
 * @head:the list itself
 * @number: to be inserted
 * Return: list with num
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *hare = (*head);
	listint_t *tortoise;
	listint_t *new_node;

	if (head == NULL)
	{
		return (NULL);
	}
	new_node = malloc(sizeof(listint_t));
	if (!new_node)
	{
		return (NULL);
	}
	if (*head == NULL)
	{
		new_node->n = number;
		new_node->next = NULL;
		*head = new_node;
		return (*head);
	}
	tortoise = *head;
	hare = (*head)->next;
	while (tortoise)
	{
		if (number < (tortoise->n))
		{
			new_node->n = number;
			new_node->next = tortoise;
			*head = new_node;
			return (*head);
		}
		else if (!hare)
		{
			new_node->n = number;
			new_node->next = NULL;
			tortoise->next = new_node;
			return (*head);
		}
		else if ((tortoise->n) <= number && (hare->n) >= number)
		{
			new_node->n = number;
			new_node->next = hare;
			tortoise->next = new_node;
			return (*head);
		}
		else
		{
			tortoise = tortoise->next;
			hare = hare->next;
		}
	}
	free(new_node);
	return (NULL);
}
