#include <stdbool.h>
#include <stdlib.h>
#include <stdio.h>


#define STRING_T 0
#define INT_T 1
#define FLOAT_T 2
#define BOOL_T 3
#define NONE_T 4

#define False false
#define True true
typedef struct Element_t {
    char *name;
    int data_type;
    char *value_str;
    int value_int;
    float value_float;
    bool value_bool;
    int is_none; // 
} Element_t;

typedef struct Stack_t {
    Element_t *elements;
    int size;
    int top;
} Stack_t;

void push(Stack_t *stack, Element_t element) {
    if (stack->top == stack->size - 1) {
        printf("ERROR : Stack is full");
        exit(1);
    }
    stack->top++;
    stack->elements[stack->top] = element;
}

void pop(Stack_t *stack) {
    if (stack->top == -1) {
        printf("ERROR : Stack is empty");
        exit(1);
    }
    stack->top--;
}

Stack_t *create_stack(int size) {
    Stack_t *stack = (Stack_t *) malloc(sizeof(Stack_t));
    stack->elements = (Element_t *) malloc(sizeof(Element_t) * size);
    stack->size = size;
    stack->top = -1;
    return stack;
}

int main() {
    Stack_t *stack = create_stack(10);
