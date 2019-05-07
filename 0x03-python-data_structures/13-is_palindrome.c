#include "lists.h"


/**
 * match_sides - recursive helper function for is_palindrome
 * @l: pointer to pointer to left side, moved right as matches found
 * @r: pointer to right side, comparisons start when it reaches end
 *
 * Return: 0 if sides don't match, 1 if they do, 2 if list is palindrome
 */
int match_sides(listint_t **l, listint_t *r)
{
	int result;

	if (r->next == NULL)
	{
		if ((*l)->n != r->n)
			return (0);
		*l = (*l)->next;
		return (1);
	}
	result = match_sides(l, r->next);
	if (result == 1)
	{
		if (*l == r)
			return (2);
		if ((*l)->n != r->n)
			return (0);
		*l = (*l)->next;
		if (*l == r)
			return (2);
		return (1);
	}
	else
	{
		return (result);
	}
}


/**
 * is_palindrome - determine whether singly-linked list is a palindrome
 * @head: pointer to pointer to first element, is not changed
 *
 * Return: 1 if list is palindrome, 0 if it isn't
 */
int is_palindrome(listint_t **head)
{
	listint_t *node;

	if (head == 0)
		return (0);
	if (*head == NULL || (*head)->next == NULL)
		return (1);
	node = *head;
	return (!!match_sides(&node, node->next));
}
