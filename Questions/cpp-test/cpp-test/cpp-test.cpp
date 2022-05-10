// cpp-test.cpp : This file contains the 'main' function. Program execution begins and ends there.
// Expected to be compiled using C++17
//

#include <algorithm>
#include <array>
#include <iostream>
#include <vector>
#include "c-test.h"

namespace CppTest
{

	class Question1Class
	{

	public:
		Question1Class()
		{
			sNumObjects++;
		}
		
		~Question1Class()
		{
			sNumObjects--;
		}

		static int nobjs()
		{
			return sNumObjects;
		}


	private:
		// Declared as int so the value may overflow to a negative number
		inline static int sNumObjects = 0;

	};

	static void PrintObjectCount()
	{
		std::cout << "Object count: " << CppTest::Question1Class::nobjs() << std::endl;
	}
	// Answer to C++ question 1
	void Question1()
	{
		const std::unique_ptr<CppTest::Question1Class> testObject1(new CppTest::Question1Class());
		CppTest::PrintObjectCount();

		for (auto i = 0; i < 5; ++i)
		{
			const std::unique_ptr<CppTest::Question1Class> testObject(new CppTest::Question1Class());
			CppTest::PrintObjectCount();
		}

		const std::unique_ptr<CppTest::Question1Class> testObject2(new CppTest::Question1Class());
		CppTest::PrintObjectCount();
		{
			const std::unique_ptr<CppTest::Question1Class> testObject3(new CppTest::Question1Class());
			CppTest::PrintObjectCount();
		}

		CppTest::PrintObjectCount();
		
	}

	struct node_t
	{
		unsigned v;
		struct node_t* next;

		explicit node_t(const unsigned val) : v(val), next(nullptr)
		{
		}
	};

	/**
	 * @brief Remove the node after node
	 * @param node the node that preceeds the node being removed
	 * @return the removed node
	 */
	struct node_t* remove_next_node(node_t** node)
	{
		node_t* nodeToRemove = nullptr;
		if (node != nullptr)
		{
			if ((*node)->next != nullptr)
			{
				// Get ref of node to remove
				nodeToRemove = (*node)->next;

				// Change next node pointer of input node
				(*node)->next = nodeToRemove->next;

				// Remove next pointer of removed node
				nodeToRemove->next = nullptr;
			}
		}
		return nodeToRemove;
	}

	void print_list(node_t* head)
	{
		if (head != nullptr)
		{
			auto currentNode = head;
			do
			{
				std::cout << currentNode->v<< " ";
				currentNode = currentNode->next;
			}
			while (currentNode != nullptr);
			std::cout << std::endl;
		}
	}

	struct node_t* even_nodes(struct node_t** head)
	{
		node_t* returnHead = nullptr;
		if (head != nullptr)
		{
			returnHead = new node_t(0);
			// Pointer to head
			auto returnNode = returnHead;
			auto previousNode = *head;
			while (previousNode != nullptr)
			{
				// Check if node that follows previousNode is even 
				if (const auto nextNode = previousNode->next; nextNode->v % 2 == 0)
				{
					const auto removedNode = remove_next_node(&previousNode);
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

	void Question2()
	{
		// Construct linked list
		auto head = new node_t(0);
		auto currentNode = head;

		// Creating an example file
		for (auto i = 1; i < 5; ++i)
		{
			const auto node = new node_t(i);
			currentNode->next = node;
			currentNode = currentNode->next;
		}
		even_nodes(nullptr);
		print_list(head);
		print_list(even_nodes(&head));
		print_list(head);
	}
}


int main(int argc, char* argv[])
{
	CppTest::Question1();
	CppTest::Question2();
}