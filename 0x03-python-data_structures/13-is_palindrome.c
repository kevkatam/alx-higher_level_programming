#include "lists.h"
/**
 * reverse - reverses the second half of the list
 * @h: head of 2nd half
 * Return: no return
 */
void reverse(listint_t **h)
{
	listint_t *prev;
	listint_t *cur;
	listint_t *nxt;

	prev = NULL;
	cur = *h;
	while (cur != NULL)
	{
		nxt = cur->next;
		cur->next = prev;
		prev = cur;
		cur = nxt;
	}
	*h = prev;
}
/**
 * compare - compares each int in the list
 * @h1: head of first half
 * @h2: head of the 2nd half
 * Return: 1 if are equals,0 if not
 */
int compare(listint_t *h1, listint_t *h2)
{
	listint_t *temp1;
	listint_t *temp2;

	temp1 = h1;
	temp2 = h2;

	while (temp1 != NULL && temp2 != NULL)
	{
		if (temp1->n == temp2->n)
		{
			temp1 = temp1->next;
			temp2 = temp2->next;
		}
		else
		{
			return (0);
		}
	}
	if (temp1 == NULL && temp2 == NULL)
	{
		return (1);
	}
	return (0);
}
/**
 * is_palindrome -  checks if a singly linked list is a palindrome.
 * @head: pointer to the head of the list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow, *fast, *prev_slow;
	listint_t *s_half, *mid;
	int isp;

	slow = fast = prev_slow = *head;
	mid = NULL;
	isp = 1;
	if (*head != NULL && (*head)->next != NULL)
	{
		while (fast != NULL && fast->next != NULL)
		{
			fast = fast->next->next;
			prev_slow = slow;
			slow = slow->next;
		}
		if (fast != NULL)
		{
			mid = slow;
			slow = slow->next;
		}
		s_half = slow;
		prev_slow->next = NULL;
		reverse(&s_half);
		isp = compare(*head, s_half);

		if (mid != NULL)
		{
			prev_slow->next = mid;
			mid->next = s_half;
		}
		else
		{
			prev_slow->next = s_half;
		}
	}
	return (isp);
}
