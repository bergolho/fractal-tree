#ifndef POINTS_H_
#define POINTS_H_

#include <cstdio>
#include <cstdlib>
#include <cstdint>

class Point_3D
{
public:
    double x, y, z;
public:
    Point_3D (const double x, const double y, const double z);
    void print ();
};

#endif