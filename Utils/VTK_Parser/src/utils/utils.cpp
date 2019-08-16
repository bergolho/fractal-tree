#include "utils.h"

void usage (const char pname[])
{
    fprintf(stderr,"%s\n",PRINT_LINE);
    fprintf(stderr,"Usage:> %s <input_filename_1> <input_filename_2> <output_filename>\n",pname);
    fprintf(stderr,"%s\n",PRINT_LINE);
    fprintf(stderr,"<input_filename_1> = First input filename (XYZ file with the points)\n");
    fprintf(stderr,"             Accepted extensions: '.txt'\n");
    fprintf(stderr,"<input_filename_2> = Second input filename (IEN file with the connections)\n");
    fprintf(stderr,"             Accepted extensions: '.txt'\n");
    fprintf(stderr,"%s\n",PRINT_LINE);
    fprintf(stderr,"Examples:\n");
    fprintf(stderr," %s inputs/LV-rabbit_xyz.txt inputs/LV-rabbit_ien.txt outputs/LV-rabbit.vtk\n",pname);
    fprintf(stderr," %s inputs/LV-rabbit_xyz.txt inputs/LV-rabbit_ien.txt outputs/LV-rabbit.vtk\n",pname);

    fprintf(stderr,"%s\n",PRINT_LINE);
}

char* get_extension_name (const char filename[])
{
    std::string base_name(filename);
    std::size_t found = base_name.find_first_of(".");

    std::string extension_name(base_name,found+1,5);

    char *result;
    result = (char*)malloc(sizeof(char)*extension_name.size()+1);
    strcpy(result,extension_name.c_str());

    return result;

}

void print_points (std::vector<struct point_3d> points)
{
    for (uint32_t i = 0; i < points.size(); i++)
        printf("%.5lf %.5lf %.5lf\n",points[i].x,points[i].y,points[i].z);
}

void print_lines (std::vector<struct line> lines)
{
    for (uint32_t i = 0; i < lines.size(); i++)
        printf("%u %u\n",lines[i].src,lines[i].dest);
}