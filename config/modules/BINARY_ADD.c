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