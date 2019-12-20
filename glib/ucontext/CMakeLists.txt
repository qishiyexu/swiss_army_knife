
SET (EXECUTABLE_OUTPUT_PATH "${CMAKE_SOURCE_DIR}/build")

set(
    DIR_UCONTEXT_SRCS
    ucontext_test.c
)

set(
    DIR_COROUTINE_TEST_SRCS
    coroutine.h
    coroutine_ucontext.c
    coroutine_test.c
    continuation.h
    continuation.c
)


add_definitions(-DWITH_UCONTEXT)

add_executable(ucontext_test ${DIR_UCONTEXT_SRCS})
target_link_libraries (ucontext_test -lgobject-2.0 -lgio-2.0 -lglib-2.0)

add_executable(coroutine_test ${DIR_COROUTINE_TEST_SRCS})
target_link_libraries (coroutine_test -lgobject-2.0 -lglib-2.0)