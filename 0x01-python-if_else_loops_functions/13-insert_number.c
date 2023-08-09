#include "lists.h"
/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: pointer to pointer of the head of the linked list
 * @number: number to be added
 * Retrun: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newnode;
	listint_t *h;

	newnode = malloc(sizeof(listint_t));
	if (newnode == NULL)
		return (NULL);
	newnode->n = number;
	h = *head;
	if (*head == NULL)
	{
		*head = newnode;
	}
	else
	{
		while (h->next <= newnode)
		{
			h = h->next;
		}
		h->next = newnode;
	}
	return (newnode);
}
