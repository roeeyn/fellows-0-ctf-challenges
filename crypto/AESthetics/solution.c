#include <stdint.h>
#include <stdlib.h>
#include <unistd.h>

uint8_t png_header[16] = {
	0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a,
	0x00, 0x00, 0x00, 0x0d, 0x49, 0x48, 0x44, 0x52
};

int
main(int argc, char **argv)
{
	uint8_t input_buffer[16];
	uint8_t output_buffer[16];
	uint8_t pad[16];
	ssize_t bytes_read;
	size_t pos = 0;

	/* read the first 16 bytes (the IV; we would need this for
	 * legitimate decryption with the key, but we don't need it to
	 * break the encryption, so we ignore these bytes
	 */
	for (int i = 0; i < 16; i++) {
		if (!read(0, input_buffer+i, 1)) {
			exit(-1);
		}
	}

	/* read the real first 16 bytes */
	for (int i = 0; i < 16; i++) {
		if (!read(0, input_buffer+i, 1)) {
			exit(-1);
		}
	}

	/* they must be the png header; xor with plaintext */
	for (int i = 0; i < 16; i++) {
		pad[i] = input_buffer[i] ^ png_header[i];
	}

	/* because the ctr implementation is buggy and reuses the
	 * counter, every block is xored with the same pad. output the
	 * header and then continue decryption.
	 */
	write(1, png_header, 16);
	while ((bytes_read = read(0, input_buffer+pos, 1)) > 0) {
		if (pos < 15) {
			pos++;
			continue;
		} else {
			for (int i = 0; i < 16; i++) {
				output_buffer[i] = input_buffer[i] ^ pad[i];
			}
			write(1, output_buffer, 16);
			pos = 0;
		}
	}

	/* we've reached EOF; decrypt any leftover bytes */
	if (pos != 0) {
		for (int i = 0; i < pos; i++) {
			output_buffer[i] = input_buffer[i] ^ pad[i];
		}
		write(1, output_buffer, pos);
	}

	return 0;
}
