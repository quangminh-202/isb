#include <iostream>
#include <cstdlib> // for srand() and rand()
#include <ctime>  //for time()

#define SIZE 128

/**
 * @brief Generate a random binary sequence of the given size.
 *
 * This function generates a random binary sequence of the given size
 * and prints it to the standard output.
 *
 * @param size The size of the binary sequence to generate.
 */
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