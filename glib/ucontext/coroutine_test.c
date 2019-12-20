#include <glib.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#include "coroutine.h"

typedef struct _UserData {
    struct coroutine* co1;
    struct coroutine* co2;
} UserData;

static gpointer func1(gpointer data)
{
    while (1) {
        printf ("I'm func1 \n");
        sleep (1);
        UserData* userdata = (UserData*)data;
        coroutine_yieldto (userdata->co2, data);
    }
    return data;

}

static gpointer func2(gpointer data)
{
    while (1) {
        printf ("I'm func2 \n");
        sleep (1);
        UserData* userdata = (UserData*)data;
        coroutine_yield (data);
    }

    return data;
}



static void test_coroutine_yield(void)
{
    UserData* ud = g_new0(UserData, 1);
    ud->co1 = g_new0(struct coroutine, 1);
    ud->co2 = g_new0(struct coroutine, 1);
    ud->co1->stack_size = 16 << 20;             //16mb
    ud->co1->entry = func1;
    ud->co2->stack_size = 16 << 20;
    ud->co2->entry = func2;
    gpointer result;

    printf ("sssss %lu\n", ud->co1->stack_size);

    coroutine_init(ud->co1);
    coroutine_init(ud->co2);
    result = coroutine_yieldto(ud->co1, ud);

}

int main()
{
    test_coroutine_yield ();
    return 0;
}