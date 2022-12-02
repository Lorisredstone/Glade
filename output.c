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

#define False false
#define True true
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

void binary_add(Stack_t *stack) {
    Element_t *element1 = pop(stack);
    Element_t *element2 = pop(stack);
    if (element1->data_type == element2->data_type && element1->data_type == INT_T) {
        Element_t *result = (Element_t *) malloc(sizeof(Element_t));
        result->data_type = INT_T;
        result->value_int = element1->value_int + element2->value_int;
        push(stack, result);
    } else if (element1->data_type == element2->data_type && element1->data_type == FLOAT_T) {
        Element_t *result = (Element_t *) malloc(sizeof(Element_t));
        result->data_type = FLOAT_T;
        result->value_float = element1->value_float + element2->value_float;
        push(stack, result);
    } else if (element1->data_type == element2->data_type && element1->data_type == STRING_T) {
        Element_t *result = (Element_t *) malloc(sizeof(Element_t));
        result->data_type = STRING_T;
        result->value_str = (char *) malloc(sizeof(char) * (strlen(element1->value_str) + strlen(element2->value_str) + 1));
        strcpy(result->value_str, element1->value_str);
        strcat(result->value_str, element2->value_str);
        push(stack, result);
    } else {
        printf("ERROR : Cannot add %d and %d", element1->data_type, element1->data_type);
        exit(1);
    }
}

int main() {
    Stack_t *stack = create_stack(10);
    // Instruction(opname='LOAD_CONST', opcode=100, arg=0, argval=1, argrepr='1', offset=0, starts_line=1, is_jump_target=False)
    Element_t *element4320 = malloc(sizeof(Element_t));
    element4320->data_type = INT_T;
    element4320->value_int = 1;
    push(stack, element4320);
    
    // Instruction(opname='STORE_NAME', opcode=90, arg=0, argval='a', argrepr='a', offset=2, starts_line=None, is_jump_target=False)
    Element_t *element1739;
    element1739 = pop(stack);
    add_variable("main_a", element1739);
    
    // Instruction(opname='LOAD_CONST', opcode=100, arg=1, argval=2, argrepr='2', offset=4, starts_line=2, is_jump_target=False)
    Element_t *element1768 = malloc(sizeof(Element_t));
    element1768->data_type = INT_T;
    element1768->value_int = 2;
    push(stack, element1768);
    
    // Instruction(opname='STORE_NAME', opcode=90, arg=1, argval='b', argrepr='b', offset=6, starts_line=None, is_jump_target=False)
    Element_t *element3229;
    element3229 = pop(stack);
    add_variable("main_b", element3229);
    
    // Instruction(opname='LOAD_NAME', opcode=101, arg=0, argval='a', argrepr='a', offset=8, starts_line=3, is_jump_target=False)
    Element_t *element1229;
    element1229 = get_variable("main_a");
    push(stack, element1229);
    
    // Instruction(opname='LOAD_NAME', opcode=101, arg=1, argval='b', argrepr='b', offset=10, starts_line=None, is_jump_target=False)
    Element_t *element1736;
    element1736 = get_variable("main_b");
    push(stack, element1736);
    
    // Instruction(opname='BINARY_ADD', opcode=23, arg=None, argval=None, argrepr='', offset=12, starts_line=None, is_jump_target=False)
    binary_add(stack);
    
    // Instruction(opname='STORE_NAME', opcode=90, arg=2, argval='c', argrepr='c', offset=14, starts_line=None, is_jump_target=False)
    Element_t *element1943;
    element1943 = pop(stack);
    add_variable("main_c", element1943);
    
    // Instruction(opname='LOAD_CONST', opcode=100, arg=2, argval=None, argrepr='None', offset=16, starts_line=None, is_jump_target=False)
    Element_t *element5550 = malloc(sizeof(Element_t));
    element5550->data_type = NONE_T;
    element5550->is_none = 1;
    push(stack, element5550);
    
    // Instruction(opname='RETURN_VALUE', opcode=83, arg=None, argval=None, argrepr='', offset=18, starts_line=None, is_jump_target=False)
    Element_t *element8645;
    element8645 = pop(stack);
    return element8645->is_none ? 0 : 1;    
}