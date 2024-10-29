#include <stddef.h>

typedef struct handle_t {
  const void *_p;
  size_t _i;
} handle_t;

typedef struct handle_pair_t {
  handle_t first;
  handle_t second;
} handle_pair_t;

handle_t new_handle(size_t index);

handle_pair_t children(handle_t h);
