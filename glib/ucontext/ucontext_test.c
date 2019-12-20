#include <ucontext.h>
#include <stdio.h>
 
void child_context_func(void * arg)
{
    printf ("child context.\n");
 
}
void context_test()
{
    char stack[1024*128];
    ucontext_t child_c,main_c;
 
    //get current context 
    getcontext(&child_c); 
    child_c.uc_stack.ss_sp        = stack;            //stack pointer
    child_c.uc_stack.ss_size      = sizeof(stack);    //stack size
    child_c.uc_stack.ss_flags     = 0;
    child_c.uc_link               = &main_c;            //context to recover when the current context is done
 
    
    makecontext(&child_c,(void (*)(void))child_context_func,0);

    //swap to child context and execute child context func
    swapcontext(&main_c,&child_c);

    printf("main context.\n");
}
 
int main()
{
    context_test();
 
    return 0;
}
