#include "point.h"

Point_3D::Point_3D (const double x, const double y, const double z)
{
    this->x = x;
    this->y = y;
    this->z = z;
}

void Point_3D::print ()
{
    printf("(%g,%g,%g)\n",this->x,this->y,this->z);
}