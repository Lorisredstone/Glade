#include <stdlib.h>
#include <stdbool.h>

typedef struct var {
    int var_type;
    int int_value;
    char *char_value;
    bool bool_value;
} var_t;

typedef struct var_list {
    var_t *var_list;
    int var_count;
    bool *var_used;
} var_list_t;

var_list_t *var_list;

void init() {
    var_list = malloc(sizeof(var_list_t));
    var_list->var_list = malloc(sizeof(var_t));
    var_list->var_count = 0;
    var_list->var_used = malloc(sizeof(bool));
}

void end() {
    free(var_list->var_list);
    for (int i = 0; i < var_list->var_count; i++) {
        if (var_list->var_used[i]) {
            if (var_list->var_list[i].var_type == 2) {
                free(var_list->var_list[i].char_value);
            }
        }
    }
}

void add_var(var_list_t var_list, var_t variable) {
    for (int i = 0; i < var_list.var_count; i++) {
        if (!var_list.var_used[i]) {
            var_list.var_list[i] = variable;
            var_list.var_used[i] = true;
            return;
        }
    }
    var_list.var_list = realloc(var_list.var_list, sizeof(var_t) * (var_list.var_count + 1));
    var_list.var_used = realloc(var_list.var_used, sizeof(bool) * (var_list.var_count + 1));
    var_list.var_list[var_list.var_count] = variable;
    var_list.var_used[var_list.var_count] = true;
    var_list.var_count++;
}

void remove_var(var_list_t var_list, int index) {
    var_list.var_used[index] = false;
}

int main(int argc, char **argv) {
    init();
    end();
}
