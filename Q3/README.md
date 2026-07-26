# Q3 – End-to-End Virtual Try-On

## Objective
The objective of Q3 was to build an end-to-end virtual try-on pipeline using an open-source virtual try-on model with the preprocessing outputs generated in Q2 (human parsing, agnostic person representation, and garment segmentation).

## Model Attempted
- CatVTON (Open-source Virtual Try-On Model)

## Environment
- Google Colab
- NVIDIA Tesla T4 GPU
- Python 3.x

## Work Completed
- Cloned the CatVTON repository.
- Installed the required dependencies.
- Prepared the person image, garment image, and preprocessing outputs generated in Q2.
- Attempted to configure and execute the virtual try-on inference pipeline.

## Challenges Encountered
During implementation, multiple dependency and compatibility issues were encountered in the current Google Colab environment. These included package conflicts, model compatibility issues, and runtime errors that prevented successful end-to-end inference. Several troubleshooting attempts were made, including reinstalling dependencies, updating package versions, and retrying the setup from a clean runtime.

Despite these efforts, a complete try-on output image could not be generated within the assessment period.

## Learning
This task provided practical experience in:
- Understanding virtual try-on pipelines.
- Integrating preprocessing outputs into downstream models.
- Managing large open-source AI repositories.
- Debugging dependency and environment compatibility issues.
- Working with GPU-based deep learning workflows.

## Repository Contents
- Q3_End_to_End_Try_On.ipynb
- Screenshots of setup and execution
- Notes documenting the implementation attempts

## Status
⚠️ Partial Implementation

The implementation demonstrates the attempted setup and integration of the virtual try-on pipeline. Although final inference could not be completed because of dependency and compatibility issues, the development process, troubleshooting steps, and intermediate work have been documented.
