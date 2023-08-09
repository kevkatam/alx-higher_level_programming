#include "lists.h"
/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: pointer to pointer of the head of the linked list
 * @number: number to be added
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newnode;
	listint_t *h;
	listint_t *prev;

	h = *head;
	newnode = malloc(sizeof(listint_t));
	if (newnode == NULL)
		return (NULL);
	while (h != NULL)
	{
		if (h->n > number)
			break;
		prev = h;
		h = h->next;
	}
	newnode->n = number;

	if (*head == NULL)
	{
		newnode->next = NULL;
		*head = newnode;
	}
	else
	{
		newnode->next = h;
		if (h == *head)
			*head = newnode;
		else
			prev->next = newnode;
	}
	return (newnode);
}
