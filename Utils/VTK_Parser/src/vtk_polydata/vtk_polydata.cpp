#include "vtk_polydata.h"


VTK_Polydata::VTK_Polydata (const char xyz_filename[], const char ien_filename[])
{
    read_points(xyz_filename);

    read_connections(ien_filename);
}

void VTK_Polydata::read_points (const char xyz_filename[])
{
    FILE *file = fopen(xyz_filename,"r");

    double pos[3];
    while (fscanf(file,"%lf %lf %lf",&pos[0],&pos[1],&pos[2]) != EOF)
    {
        Point_3D point(pos[0],pos[1],pos[2]);

        this->points.push_back(point);
    }

    fclose(file);

    //printf("Number of points = %lu\n",this->points.size());
}

void VTK_Polydata::read_connections (const char ien_filename[])
{
    FILE *file = fopen(ien_filename,"r");

    uint32_t conn[2];
    while (fscanf(file,"%d %d",&conn[0],&conn[1]) != EOF)
    {
        Line line(conn[0],conn[1]);

        this->lines.push_back(line);
    }

    fclose(file);

    //printf("Number of lines = %lu\n",this->lines.size());
}

void VTK_Polydata::write_to_vtk (const char vtk_filename[])
{
    FILE *file = fopen(vtk_filename,"w+");

    fprintf(file,"# vtk DataFile Version 3.0\n");
    fprintf(file,"Purkinje\n");
    fprintf(file,"ASCII\n");
    fprintf(file,"DATASET POLYDATA\n");
    fprintf(file,"POINTS %lu float\n",this->points.size());
    for (uint32_t i = 0; i < this->points.size(); i++)
        fprintf(file,"%g %g %g\n",this->points[i].x,this->points[i].y,this->points[i].z);
    fprintf(file,"LINES %lu %lu\n",this->lines.size(),this->lines.size()*3);
    for (uint32_t i = 0; i < this->lines.size(); i++)
        fprintf(file,"2 %u %u\n",this->lines[i].src,this->lines[i].dest);

    fclose(file);
}