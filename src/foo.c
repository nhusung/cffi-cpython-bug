#include <stdio.h>

#include "foo.h"

handle_t new_handle(size_t index) {
  handle_t h = {._p = NULL, ._i = index};
  return h;
}

handle_pair_t children(handle_t h) {
  handle_pair_t pair;

  // just write come pointer value
  pair.first._p = pair.second._p = h._p == NULL ? (void *)children : NULL;

  // write some index values
  pair.first._i = h._i + 20;
  pair.second._i = h._i + 100;

  printf("children({._p = %p, ._i = %zu}) = {.first = {._p = %p, ._i = %zu}, "
         ".second = {._p = %p, ._i = %zu}}\n",
         h._p, h._i, pair.first._p, pair.first._i, pair.second._p,
         pair.second._i);

  return pair;
}
