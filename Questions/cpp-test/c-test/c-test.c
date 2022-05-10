// c-test.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <stdio.h>
#include <stdlib.h>

typedef struct node_t
{
	unsigned v;
	struct node_t* next;

} node_t;


node_t* CreateNode(const unsigned val)
{
	node_t* node = malloc(sizeof(node_t));
	node->v = val;
	node->next = NULL;
	return node;
}

/**
 * @brief Remove the node after node
 * @param node the node that preceeds the node being removed
 * @return the removed node
 */
struct node_t* remove_next_node(node_t** node)
{
	node_t* nodeToRemove = NULL;
	if (node != NULL)
	{
		if ((*node)->next != NULL)
		{
			// Get ref of node to remove
			nodeToRemove = (*node)->next;

			// Change next node pointer of input node
			(*node)->next = nodeToRemove->next;

			// Remove next pointer of removed node
			nodeToRemove->next = NULL;
		}
	}
	return nodeToRemove;
}

struct node_t* even_nodes(struct node_t** head)
{
	node_t* returnHead = NULL;
	if (head != NULL)
	{
		returnHead = CreateNode(0);
		// Pointer to head
		node_t* returnNode = returnHead;
		node_t* previousNode = *head;
		while (previousNode != NULL)
		{
			// Check if node that follows previousNode is even 
			if (previousNode->next->v % 2 == 0)
			{
				const node_t* removedNode = remove_next_node(&previousNode);
				// Add removed node to return node (linked list of nodes with even values)
				returnNode->next = removedNode;
				returnNode = returnNode->next;
			}
			// Increment the previous node
			previousNode = previousNode->next;
		}
		returnHead = returnHead->next;
	}
	// Remove head
	return returnHead;
}



void print_list(node_t* head)
{
	if (head != NULL)
	{
		node_t* currentNode = head;
		do
		{
			printf("%u ", currentNode->v);
			currentNode = currentNode->next;
		} while (currentNode != NULL);
		printf("\n");
	}
}

void Question1()
{
	// Construct linked list
	node_t* head = CreateNode(0);
	node_t* currentNode = head;

	// Creating an example file
	for (int i = 1; i < 5; ++i)
	{
		node_t* node = CreateNode(i);
		currentNode->next = node;
		currentNode = currentNode->next;
	}
	even_nodes(NULL);
	print_list(head);
	print_list(even_nodes(&head));
	print_list(head);
}

int main()
{
	Question1();
}

// Run program: Ctrl + F5 or Debug > Start Without Debugging menu
// Debug program: F5 or Debug > Start Debugging menu

// Tips for Getting Started: 
//   1. Use the Solution Explorer window to add/manage files
//   2. Use the Team Explorer window to connect to source control
//   3. Use the Output window to see build output and other messages
//   4. Use the Error List window to view errors
//   5. Go to Project > Add New Item to create new code files, or Project > Add Existing Item to add existing code files to the project
//   6. In the future, to open this project again, go to File > Open > Project and select the .sln file
