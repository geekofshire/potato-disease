#include <stdio.h>
#include <stdlib.h>

// Function to calculate the parity bit for a given data bit position
int calculate_parity_bit(int data[], int position, int n) {
    int parity_bit = 0;
    for (int i = position - 1; i < n; i += position * 2) {
        for (int j = 0; j < position && i + j < n; j++) {
            parity_bit ^= data[i + j];
        }
    }
    return parity_bit;
}

// Function to encode the data using Hamming code
void hamming_encode(int data[], int n) {
    int m = 0;
    while ((1 << m) <= n + m + 1) {
        m++;
    }
    int encoded[n + m];
    int p = 0;
    for (int i = 0; i < n + m; i++) {
        if ((i & (i + 1)) == 0) {
            encoded[i] = 0;
        } else {
            encoded[i] = data[p++];
        }
    }
    for (int i = 0; i < m; i++) {
        int position = 1 << i;
        encoded[position - 1] = calculate_parity_bit(encoded, position, n + m);
    }
    printf("Encoded Data: ");
    for (int i = 0; i < n + m; i++) {
        printf("%d", encoded[i]);
    }
    printf("\n");
}

// Function to decode the data using Hamming code
void hamming_decode(int encoded[], int n) {
    int m = 0;
    while ((1 << m) <= n) {
        m++;
    }
    int error_position = 0;
    for (int i = 0; i < m; i++) {
        int position = 1 << i;
        int parity_bit = calculate_parity_bit(encoded, position, n);
        if (encoded[position - 1] != parity_bit) {
            error_position += position;
        }
    }
    if (error_position > 0) {
        printf("Error Detected at Bit Position: %d\n", error_position);
        encoded[error_position - 1] ^= 1;
        printf("Corrected Data: ");
    } else {
        printf("No Error Detected: ");
    }
    for (int i = 0; i < n; i++) {
        if ((i & (i + 1)) != 0) {
            printf("%d", encoded[i]);
        }
    }
    printf("\n");
}

int main() {
    int n;
    printf("Enter the number of data bits: ");
    scanf("%d", &n);
    int data[n];
    printf("Enter the data bits: ");
    for (int i = 0; i < n; i++) {
        scanf("%d", &data[i]);
    }
    hamming_encode(data, n);
    int m = 0;
    while ((1 << m) <= n + m + 1) {
        m++;
    }
    int encoded[n + m];
    printf("Enter the encoded data bits: ");
    for (int i = 0; i < n + m; i++) {
        scanf("%d", &encoded[i]);
    }
    hamming_decode(encoded, n + m);
    return 0;
}