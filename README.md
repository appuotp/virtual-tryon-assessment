# Virtual Try-On Assessment

Author: Amruth Krishnan M  
Degree: Master of Computer Applications (MCA)

## Overview

This repository contains my submission for the Virtual Try-On Assessment. The project is divided into separate tasks covering garment understanding, human parsing, virtual try-on, and a demonstration web application.

The implementation focuses on computer vision, image segmentation, and multimodal AI models using Google Colab and open-source frameworks.

---

## Repository Structure

Virtual-TryOn-Assessment/
│
├── Q1/
├── Q2/
├── Q3/
├── Q5/
└── README.md
---

## Q1 – Garment & Body Understanding

### Objective
Extract garment and body attributes from an input image using a Vision Language Model (VLM).

### Model Used
- Qwen2.5-VL

### Output
- Structured JSON containing garment attributes.

---

## Q2 – Human Parsing & Garment Segmentation

### Objective
Generate the preprocessing inputs required for virtual try-on.

### Models Used
- SegFormer Human Parsing
- Segment Anything Model (SAM)
- rembg

### Outputs
- Human Parsing Map
- Agnostic Person Image
- Garment Mask

---

## Q3 – End-to-End Virtual Try-On

### Objective
Generate virtual try-on images using an open-source virtual try-on model.

### Model Attempted
- CatVTON

### Status
The repository was successfully configured and multiple implementation attempts were made. However, dependency and compatibility issues prevented successful end-to-end inference within the assessment period.

The implementation steps and observations have been documented in the Q3 folder.

---

## Q5 – Web Demonstration

A Gradio-based web application was developed to demonstrate the completed components of the assessment.

### Features

- Display Q1 garment understanding output
- Display Q2 human parsing map
- Display agnostic person representation
- Display garment mask
- Display implementation status for Q3 and Q4

---

## Technologies Used

- Python
- Google Colab
- Gradio
- PyTorch
- Hugging Face Transformers
- OpenCV
- Pillow
- Segment Anything Model (SAM)
- SegFormer
- rembg
- Git & GitHub

---

## Repository Contents

- Source code
- Google Colab notebooks
- Generated outputs
- Documentation
- Screenshots

---

## Demo Video

A demonstration video of the implementation has been recorded.

Google Drive Link:

*(Add your Google Drive video link here)*

---

## GitHub Repository

*(Add your GitHub repository link here)*

---

## Notes

- Q1 and Q2 were successfully completed.
- Q3 documents the implementation attempts and encountered compatibility issues.
- The Gradio web application demonstrates the completed modules.
- The project was developed and tested using Google Colab.

---

## Author

Amruth Krishnan M

amruth.krish007@gmail.com

2026
