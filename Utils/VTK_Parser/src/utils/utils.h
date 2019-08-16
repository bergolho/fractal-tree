#ifndef UTILS_H_
#define UTILS_H_

#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cstdint>

#include <string>
#include <vector>

#define PRINT_LINE "========================================================================================================================="
#define UM_TO_MM 0.001

struct point_3d
{
    double x;
    double y;
    double z;
};

struct line
{
    uint32_t src;
    uint32_t dest;
};

void usage (const char pname[]);
char* get_extension_name (const char filename[]);

void print_points (std::vector<struct point_3d> points);
void print_lines (std::vector<struct line> lines);

#endif