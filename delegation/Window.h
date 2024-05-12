#ifndef DELEGATION_WINDOW_H
#define DELEGATION_WINDOW_H

#include "Shape.h"
#include "Rectangle.h"
#include "Circle.h"

class Window
{
private:
    Shape* shape;
public:
    Window (Shape* shape) : shape (shape) { }
    double area();
};


#endif //DELEGATION_WINDOW_H
