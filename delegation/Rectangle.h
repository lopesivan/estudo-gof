#ifndef DELEGATION_RECTANGLE_H
#define DELEGATION_RECTANGLE_H

#include "Shape.h"

class Rectangle : public Shape
{

private:
    double height;
    double width;

public:
    double area();

    Rectangle (double height, double width) : height (height), width (width) { }

};


#endif //DELEGATION_RECTANGLE_H
