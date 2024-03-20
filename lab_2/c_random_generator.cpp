#include <iostream>
#include <cstdlib>
#include <ctime>

#define SIZE 128

void random(int size) {
    srand(time(NULL));
    for (int i = 0; i < size; ++i) {
        std::cout << rand() % 2;
    }
}

int main() {
    random(SIZE);
    return 0;
}