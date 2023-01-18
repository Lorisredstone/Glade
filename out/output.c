#include <stdbool.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

// definition of tuypes
#define STRING_T 0
#define INT_T 1
#define FLOAT_T 2
#define BOOL_T 3
#define NONE_T 4

typedef struct Element_t {
    int data_type;
    char *value_str;
    int value_int;
    float value_float;
    bool value_bool;
    int is_none; // use 0 for false and 1 for true
} Element_t;

// definition of the stack
typedef struct Stack_t {
    Element_t **elements;
    int size;
    int top;
} Stack_t;

void push(Stack_t *stack, Element_t *element) {
    if (stack->top == stack->size - 1) {
        printf("ERROR : Stack is full");
        exit(1);
    }
    stack->top++;
    stack->elements[stack->top] = element;
}

Element_t *pop(Stack_t *stack) {
    if (stack->top == -1) {
        printf("ERROR : Stack is empty");
        exit(1);
    }
    stack->top--;
    return stack->elements[stack->top + 1];
}

Stack_t *create_stack(int size) {
    Stack_t *stack = (Stack_t *) malloc(sizeof(Stack_t));
    stack->elements = (Element_t **) malloc(sizeof(Element_t) * size);
    stack->size = size;
    stack->top = -1;
    return stack;
}

// variable space
#define MAX_VARIABLES 100
Element_t *variables[MAX_VARIABLES];
char *variable_names[MAX_VARIABLES];
int variable_count = 0;

void add_variable(char *name, Element_t *element) {
    if (variable_count == MAX_VARIABLES) {
        printf("ERROR : Too many variables");
        exit(1);
    }
    // we look if the variable already exists
    int index = variable_count;
    for (int i = 0; i < variable_count; i++) {
        if (strcmp(name, variable_names[i]) == 0) {
            index = i;
            break;
        }
    }
    variables[index] = element;
    variable_names[index] = name;
    if (index == variable_count) {
        variable_count++;
    }
}

Element_t *get_variable(char *name) {
    for (int i = 0; i < variable_count; i++) {
        if (strcmp(name, variable_names[i]) == 0) {
            return variables[i];
        }
    }
    printf("ERROR : Variable %s not found", name);
    exit(1);
}

void remove_variable(char *name) {
    for (int i = 0; i < variable_count; i++) {
        if (strcmp(name, variable_names[i]) == 0) {
            for (int j = i; j < variable_count - 1; j++) {
                variables[j] = variables[j + 1];
                variable_names[j] = variable_names[j + 1];
            }
            variable_count--;
            return;
        }
    }
    printf("ERROR : Variable %s not found", name);
    exit(1);
}

int main() {
    Stack_t *stack = create_stack(10);
    // Instruction(opname='LOAD_CONST', opcode=100, arg=0, argval=1, argrepr='1', offset=0, starts_line=1, is_jump_target=False)
    Element_t *element7747 = malloc(sizeof(Element_t));
    element7747->data_type = INT_T;
    element7747->value_int = 1;
    push(stack, element7747);
    
    // Instruction(opname='STORE_NAME', opcode=90, arg=0, argval='a', argrepr='a', offset=2, starts_line=None, is_jump_target=False)
    Element_t *element8017;
    element8017 = pop(stack);
    add_variable("main_a", element8017);
    
    // Instruction(opname='LOAD_CONST', opcode=100, arg=1, argval=2, argrepr='2', offset=4, starts_line=2, is_jump_target=False)
    Element_t *element1942 = malloc(sizeof(Element_t));
    element1942->data_type = INT_T;
    element1942->value_int = 2;
    push(stack, element1942);
    
    // Instruction(opname='STORE_NAME', opcode=90, arg=1, argval='b', argrepr='b', offset=6, starts_line=None, is_jump_target=False)
    Element_t *element9532;
    element9532 = pop(stack);
    add_variable("main_b", element9532);
    
    // Instruction(opname='LOAD_CONST', opcode=100, arg=2, argval=None, argrepr='None', offset=8, starts_line=None, is_jump_target=False)
    Element_t *element1995 = malloc(sizeof(Element_t));
    element1995->data_type = NONE_T;
    element1995->is_none = 1;
    push(stack, element1995);
    
    // Instruction(opname='RETURN_VALUE', opcode=83, arg=None, argval=None, argrepr='', offset=10, starts_line=None, is_jump_target=False)
    Element_t *element6572;
    element6572 = pop(stack);
    return element6572->is_none ? 0 : 1;    
}