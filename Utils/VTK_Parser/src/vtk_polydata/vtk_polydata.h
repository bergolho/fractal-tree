#ifndef VTK_POLYDATA_H_
#define VTK_POLYDATA_H_

#include <cstdio>
#include <cstdlib>
#include <cstdint>

#include <vector>

#include "../utils/utils.h"

#include "point.h"
#include "line.h"

class VTK_Polydata
{
public:
    std::vector<Point_3D> points;
    std::vector<Line> lines;
public:
    VTK_Polydata (const char xyz_filename[], const char ien_filename[]);
    void read_points (const char xyz_filename[]);
    void read_connections (const char ien_filename[]);
    void write_to_vtk (const char vtk_filename[]);
};

#endif