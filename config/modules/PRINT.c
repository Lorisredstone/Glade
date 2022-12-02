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