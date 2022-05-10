#pragma once

typedef struct node_t
{
	unsigned v;
	struct node_t* next;

} node_t;


node_t* CreateNode(const unsigned val);

/**
 * @brief Remove the node after node
 * @param node the node that preceeds the node being removed
 * @return the removed node
 */
struct node_t* remove_next_node(node_t** node);

struct node_t* even_nodes(struct node_t** head);



void print_list(node_t* head);

void Question1();

unsigned char reverse_byte(const unsigned char byte);

void reverse_bytes(unsigned char* buf, unsigned int bufSize);