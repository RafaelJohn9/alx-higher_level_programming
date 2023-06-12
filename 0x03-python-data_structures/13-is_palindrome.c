#include "lists.h"
#include <stdlib.h>
/**
 * is_palindrome-checks if a singly linked list is palindrome
 * @head:pointer to linked list
 * Return:boolean
 */
int is_palindrome(listint_t **head)
{
        if (*head == NULL || (*head)->next == NULL)
                return (1);

        listint_t *slow = *head;
        listint_t *fast = *head;
        listint_t *prev = NULL;
        listint_t *temp;

        while (fast != NULL && fast->next != NULL)
        {
                fast = fast->next->next;

                // Reverse the first half of the list
                temp = slow;
                slow = slow->next;
                temp->next = prev;
                prev = temp;
        }

        // If the list has odd number of elements, skip the middle element
        if (fast != NULL)
                slow = slow->next;

        // Compare the reversed first half with the second half
        while (slow != NULL)
        {
                if (slow->n != prev->n)
                        return (0);
                slow = slow->next;
                prev = prev->next;
        }

        return (1);
}
