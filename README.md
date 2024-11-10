# RF-Based Ranging for Relative Localization

## "Walking Skeleton"

- To begin, we have initialized our repository to contain all of the necessary documents and API references needed for development
  - An API reference can be found in `/Doc/DW3xxx_Driver_API_Guide_6.0.14.pdf`
  - A guide for using the software development kit (SDK) can be found in `/Doc/DWM3001CDK_SDK_Developer_Guide_0.1.1.pdf`
- We are still awaiting the arrival of at least one micro-USB to USB-A adapter for communication with devices
  - The first task in our next sprint will be writing and testing a basic "hello word" equivalent program on the devices

## Connectivity List
- The vast majority of the effort on this project went into developing custom firmware for the DWM3001C boards. The first step was developing custom firmware that could measure the distance to another device. This task took the longest. The next task was to develop firmware such that one board (an initiator) can measure the distance between itself and some arbitrary amount of other boards (responders). These distances are stored in what's known as a **connectivity list**.

- We have successfully developed custom firmware to build a connectivity list. This firmware can be found at [DWM3001CDK-rf-ranging](https://github.com/owenc21/DWM3001CDK-rf-ranging)
  - The linked repository contains the custom firmware, instructions for use, and a more detailed view of what it does and how
  - Developing this firmware represents the bulk of the semester's effort