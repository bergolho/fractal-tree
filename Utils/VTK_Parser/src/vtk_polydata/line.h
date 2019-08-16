#ifndef LINE_H_
#define LINE_H_

#include <cstdio>
#include <cstdlib>
#include <cstdint>

class Line
{
public:
    uint32_t src;
    uint32_t dest;
public:
    Line (const uint32_t src, const uint32_t dest);
    void print ();
};

#endif