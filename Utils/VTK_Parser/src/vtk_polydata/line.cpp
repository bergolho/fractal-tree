#include "line.h"

Line::Line (const uint32_t src, const uint32_t dest)
{
    this->src = src;
    this->dest = dest;
}

void Line::print ()
{
    printf("(%u,%u)\n",this->src,this->dest);
}