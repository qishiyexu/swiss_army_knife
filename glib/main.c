#include <stdlib.h>
#include <stdio.h>
#include <glib.h>

int main(int argc, char* argv[])
{
    char* version = "1.13.0-test";
    printf ("hello!\n");
    int nversion = 14001;
    char** splitted = g_strsplit (version, "-", -1);
    if (splitted && splitted[0]) {
        char** sub_splitted = g_strsplit(splitted[0], ".", -1);
        if (sub_splitted) {
            if (sizeof(sub_splitted) >= 3 && g_ascii_isdigit(*sub_splitted[0]) && 
                        g_ascii_isdigit(*sub_splitted[1]) && g_ascii_isdigit(*sub_splitted[2])) {
                printf ("%s \n", sub_splitted[0]);
                printf ("%s \n", sub_splitted[1]);
                printf ("%s \n", sub_splitted[2]);
                nversion = atoi(sub_splitted[0]) * 1000000 + atoi(sub_splitted[1]) * 1000 + atoi(sub_splitted[2]);
                printf ("nversion: %d\n", nversion);
            }
            g_strfreev(sub_splitted);
        }

        g_strfreev(splitted);
    }
    char tmp_version[32];
    memset(tmp_version, 0, 32);
    snprintf(tmp_version, 32, "%d", nversion);
    printf ("tmp_version: %s\n", tmp_version);

    return 0;
}