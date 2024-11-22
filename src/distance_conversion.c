#include <stdio.h>
#include <math.h>
#include <stdlib.h>

/* RSSI signal strength decreases logarithmically with distance
 * If using signal strength to measure distance, you need to calculate an exponential
 * This can take significant time, and RSSI signals can fluctuate enough that precise calculations aren't very useful
 * Solution: save a bunch of precalculated results to a table and interpolate between them
 * The devices are already imprecise so a fairly crude approximation is sufficient
 */


//can be changed depending on what is useful
const int min = 60, 		//-60db = ~.5m
	max = 90,				//-90db = ~50m 
	range = max-min,		//if you find a reason to change this, let me know
	dmap_length = 256; 		//floats are 4 bytes, table is 1kb 
	
//the table
float* dmap;


//Conversion function to be called by outside programs
//Converts RSSI into an index and returns a value interpolated between two table values, or -1 if the RSSI is too big or small to be useful

float distance(float rssi){
	//devices are wildly inaccurate outside of [-70, -85]; if an RSSI value is too far outside of this range, disregard it
	if(-rssi < min || -rssi > max) return -1;
	
	//scaling rssi value to the range [0, 256] and splitting into integer and fractional parts
	float rssi_shift = ((-rssi) - min) * (float)dmap_length/range;
	float t = rssi_shift - (int)(rssi_shift);
	int index = (int)rssi_shift;
	
	//linear interpolation
	float interp = dmap[index] + (dmap[index + 1] - dmap[index])*t;
	
	return interp;
	
}


//Deallocate the table if necessary

void close_distance(){
	if (dmap != NULL) free(dmap);

}


//Table initialization

int init_distance(){
	dmap = malloc(sizeof(float)*dmap_length);
	
	float rssi;
	
	for(int i = 0; i < dmap_length; i++){
		//convert i into to a feasible rssi signal strength between the defined bounds
		rssi = -(i * ((float)range/dmap_length) + min);
		
		//approximate model based on measurements taken, accurate to ~10cm, within range of random variance devices showed
		dmap[i] = expf(-(rssi + 65.3)/6.3);
	
	}

}
