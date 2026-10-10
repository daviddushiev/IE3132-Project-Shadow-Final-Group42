#include <stdio.h>
#include <stddef.h>

static const unsigned char KEY[] = "NIGHTFALL";

__attribute__((noinline))
void archive_transform(unsigned char *data, size_t length) {
    size_t key_length = sizeof(KEY) - 1;

    for (size_t i = 0; i < length; i++) {
        data[i] ^= KEY[i % key_length];
    }
}

int main(void) {
    unsigned char marker[] = {'S', 'H', 'A', 'D', 'O', 'W'};

    archive_transform(marker, sizeof(marker));

    unsigned int checksum = 0;

    for (size_t i = 0; i < sizeof(marker); i++) {
        checksum = (checksum * 33u) ^ marker[i];
    }

    printf("Shadow Archive Utility v1.0\n");
    printf("Archive subsystem ready.\n");
    printf("Header verification: %u\n", checksum);

    return 0;
}
