SOLAR PANEL FAULT DETECTION SYSTEM
================================

This project presents an AI-based system for detecting faults in solar panels using thermal images. The system applies deep learning techniques to automatically identify common solar panel faults and provide clear, actionable insights through a web-based interface.

The project is intended to support faster inspection, early fault detection, and improved maintenance decision-making in solar energy systems.

PROJECT OVERVIEW
----------------
Solar panel faults can significantly reduce system efficiency and reliability. Traditional inspection methods are often slow, costly, and sometimes unsafe. This project addresses these challenges by using computer vision to analyze thermal images and classify fault conditions automatically.

Users can upload a thermal image or select a sample image to receive an instant fault diagnosis, including the detected fault type, severity level, estimated efficiency loss, and recommended corrective action.

KEY CAPABILITIES
----------------
The system enables automated fault detection from thermal images and presents results in a simple and intuitive interface. It provides fault classification with confidence estimation, severity assessment, and maintenance guidance. The application also includes sample images for demonstration purposes and a basic fault management view for monitoring detected issues.

FAULT TYPES SUPPORTED
---------------------
The trained model supports multiple solar panel conditions, including hot spots, cell faults, cracking, diode faults, soiling, shadowing, vegetation interference, and normal operation with no detected anomaly. Each detected fault is associated with an impact level and recommended maintenance response.

DEPLOYMENT
----------
The application is deployed as a web-based interface using Streamlit and is configured for cloud deployment. Only the essential files required for inference and demonstration are included in the repository. Development and training artifacts are excluded to keep the project lightweight and deployment-ready.

AUTHOR
------
Emmanuel Bilson  
Electrical and Electronics Engineering  
Focus on Renewable Energy Systems and Artificial Intelligence
