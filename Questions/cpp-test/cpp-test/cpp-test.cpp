// cpp-test.cpp : This file contains the 'main' function. Program execution begins and ends there.
// Expected to be compiled using C++17
//

#include <iostream>

namespace CppTest
{

	class TestClass
	{

	public:
		TestClass()
		{
			sNumObjects++;
		}
		
		~TestClass()
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
		std::cout << "Object count: " << CppTest::TestClass::nobjs() << std::endl;
	}
	// Answer to C++ question 1
	void Question1()
	{
		const std::unique_ptr<CppTest::TestClass> testObject1(new CppTest::TestClass());
		CppTest::PrintObjectCount();

		for (auto i = 0; i < 5; ++i)
		{
			const std::unique_ptr<CppTest::TestClass> testObject(new CppTest::TestClass());
			CppTest::PrintObjectCount();
		}

		const std::unique_ptr<CppTest::TestClass> testObject2(new CppTest::TestClass());
		CppTest::PrintObjectCount();
		{
			const std::unique_ptr<CppTest::TestClass> testObject3(new CppTest::TestClass());
			CppTest::PrintObjectCount();
		}

		CppTest::PrintObjectCount();
		
	}
}



int main(int argc, char* argv[])
{
	CppTest::Question1();

}