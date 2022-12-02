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

void print(Stack_t *stack, int nb_args) {
    Element_t **elements = (Element_t **) malloc(sizeof(Element_t) * nb_args);
    for (int i = 0; i < nb_args; i++) {
        elements[i] = pop(stack);
    }
    for (int i = nb_args - 1; i >= 0; i--) {
        if (elements[i]->data_type == INT_T) {
            printf("%d", elements[i]->value_int);
        } else if (elements[i]->data_type == FLOAT_T) {
            printf("%f", elements[i]->value_float);
        } else if (elements[i]->data_type == STRING_T) {
            printf("%s", elements[i]->value_str);
        } else {
            printf("ERROR : Cannot print %d", elements[i]->data_type);
            exit(1);
        }
    }
    // we add a newline at the end
    printf("\n");
    // than we free the elements
    for (int i = 0; i < nb_args; i++) {
        free(elements[i]);
    }
    free(elements);
    // than we add a none element to the stack
    Element_t *none = (Element_t *) malloc(sizeof(Element_t));
    none->data_type = NONE_T;
    none->is_none = 1;
    push(stack, none);
}

int main() {
    Stack_t *stack = create_stack(10);
    // Instruction(opname='LOAD_CONST', opcode=100, arg=0, argval=1, argrepr='1', offset=0, starts_line=1, is_jump_target=False)
    Element_t *element4524 = malloc(sizeof(Element_t));
    element4524->data_type = INT_T;
    element4524->value_int = 1;
    push(stack, element4524);
    
    // Instruction(opname='STORE_NAME', opcode=90, arg=0, argval='a', argrepr='a', offset=2, starts_line=None, is_jump_target=False)
    Element_t *element8525;
    element8525 = pop(stack);
    add_variable("main_a", element8525);
    
    // Instruction(opname='LOAD_CONST', opcode=100, arg=1, argval=2, argrepr='2', offset=4, starts_line=2, is_jump_target=False)
    Element_t *element5815 = malloc(sizeof(Element_t));
    element5815->data_type = INT_T;
    element5815->value_int = 2;
    push(stack, element5815);
    
    // Instruction(opname='STORE_NAME', opcode=90, arg=1, argval='b', argrepr='b', offset=6, starts_line=None, is_jump_target=False)
    Element_t *element2271;
    element2271 = pop(stack);
    add_variable("main_b", element2271);
    
    // Instruction(opname='LOAD_NAME', opcode=101, arg=0, argval='a', argrepr='a', offset=8, starts_line=3, is_jump_target=False)
    Element_t *element7077;
    element7077 = get_variable("main_a");
    push(stack, element7077);
    
    // Instruction(opname='LOAD_NAME', opcode=101, arg=1, argval='b', argrepr='b', offset=10, starts_line=None, is_jump_target=False)
    Element_t *element7602;
    element7602 = get_variable("main_b");
    push(stack, element7602);
    
    // Instruction(opname='BINARY_ADD', opcode=23, arg=None, argval=None, argrepr='', offset=12, starts_line=None, is_jump_target=False)
    binary_add(stack);
    
    // Instruction(opname='STORE_NAME', opcode=90, arg=2, argval='c', argrepr='c', offset=14, starts_line=None, is_jump_target=False)
    Element_t *element4938;
    element4938 = pop(stack);
    add_variable("main_c", element4938);
    
    // Instruction(opname='LOAD_NAME', opcode=101, arg=3, argval='print', argrepr='print', offset=16, starts_line=4, is_jump_target=False)
    Element_t *element4149;
    element4149 = get_variable("main_print");
    push(stack, element4149);
    
    // Instruction(opname='LOAD_NAME', opcode=101, arg=2, argval='c', argrepr='c', offset=18, starts_line=None, is_jump_target=False)
    Element_t *element6064;
    element6064 = get_variable("main_c");
    push(stack, element6064);
    
    // Instruction(opname='CALL_FUNCTION', opcode=131, arg=1, argval=1, argrepr='', offset=20, starts_line=None, is_jump_target=False)
    // Instruction(opname='POP_TOP', opcode=1, arg=None, argval=None, argrepr='', offset=22, starts_line=None, is_jump_target=False)
    pop(stack);
    
    // Instruction(opname='LOAD_CONST', opcode=100, arg=2, argval=None, argrepr='None', offset=24, starts_line=None, is_jump_target=False)
    Element_t *element5807 = malloc(sizeof(Element_t));
    element5807->data_type = NONE_T;
    element5807->is_none = 1;
    push(stack, element5807);
    
    // Instruction(opname='RETURN_VALUE', opcode=83, arg=None, argval=None, argrepr='', offset=26, starts_line=None, is_jump_target=False)
    Element_t *element7996;
    element7996 = pop(stack);
    return element7996->is_none ? 0 : 1;    
}