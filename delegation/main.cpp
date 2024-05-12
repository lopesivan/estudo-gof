#include <iostream>

#include "Window.h"

using namespace std;


int main() {
    cout << "Hello, World!" << endl;
    Window *window = new Window(new Rectangle(2.3, 44));
    cout << window->area() << "\n";

    window = new Window(new Circle(4));
    cout << window->area() << "\n";

    return 0;
}