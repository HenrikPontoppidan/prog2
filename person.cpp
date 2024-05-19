#include <cstdlib>
// Person class 

class Person{
	public:
		Person(int);
		int getAge();
		void setAge(int);
		double getDecades();
		int fib(int);
	private:
		int age;
		int fib_p(int);
	};
 
Person::Person(int a){
	age = a;
	}
 
int Person::fib_p(int n){
	if (n <= 1){
		return n;
	}
	else{
		return fib_p(n-1) + fib_p(n-2);
	}
}

int Person::fib(){
	return fib(age);
}

int Person::getAge(){
	return age;
	}
 
void Person::setAge(int a){
	age = a;
	}

double Person::getDecades(){
	return age/10.0;
	}


extern "C"{
	Person* Person_new(int a) {return new Person(a);}
	int Person_getAge(Person* person) {return person->getAge();}
	void Person_setAge(Person* person, int a) {person->setAge(a);}
	double Person_getDecades(Person* person) {return person->getDecades();}
	int Person_fib(Person* person) {return person->fib();}
	void Person_delete(Person* person){
		if (person){
			delete person;
			person = nullptr;
			}
		}
	}