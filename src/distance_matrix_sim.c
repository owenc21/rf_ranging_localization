/**
 * A very basic example simulation of building a distance matrix of N devices
 * in a network, from the perspective of device 1
 */

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define N 5 // Total number of devices in the network
#define DEVICE_ID 1 // Device "1" is our target device for building the matrix

// Function to simulate distance measurement between two devices
float get_distance(int device_a, int device_b) {
    // Using a random distance between 1 and 100
    return (float)(rand() % 100 + 1);
}

int main() {
    float distance_matrix[N][N];
    int i, j;

    srand(time(NULL));

    // Initialize the distance matrix for device "1"
    for (i = 0; i < N; i++) {
        for (j = 0; j < N; j++) {
            if (i == j) {
                // Distance from a device to itself is 0
                distance_matrix[i][j] = 0.0f;
            } else {
                // Simulate getting distance from i to j
                distance_matrix[i][j] = get_distance(i, j);
            }
        }
    }

    // Print the distance matrix for verification
    printf("Distance Matrix for Device %d:\n", DEVICE_ID);
    for (i = 0; i < N; i++) {
        for (j = 0; j < N; j++) {
            printf("%6.2f ", distance_matrix[i][j]);
        }
        printf("\n");
    }

    return 0;
}
