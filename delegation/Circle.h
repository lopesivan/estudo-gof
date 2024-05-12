#ifndef DELEGATION_CIRCLE_H
#define DELEGATION_CIRCLE_H


#include "Shape.h"

class Circle: public Shape
{
private:
    double radius;

public:
    double area();

    Circle (double radius) : radius (radius) { }
};


#endif //DELEGATION_CIRCLE_H
