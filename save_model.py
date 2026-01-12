"""
Model Packager for Solar Fault Detection
"""

import os
import shutil
from pathlib import Path
import json
from datetime import datetime

print("="*60)
print("SOLAR FAULT DETECTION - MODEL PACKAGING")
print("="*60)

os.makedirs('models', exist_ok=True)
print("\n✓ Created models directory")

print("\n1/3 Copying YOLOv8 model...")
source_model = 'runs/classify/solar_fault_detection/weights/best.pt'
target_model = 'models/solar_fault_model.pt'

if Path(source_model).exists():
    shutil.copy(source_model, target_model)
    model_size = os.path.getsize(target_model) / (1024*1024)
    print(f"   ✓ Model copied ({model_size:.1f} MB)")
else:
    print(f"   ✗ Model not found at: {source_model}")
    exit(1)

print("\n2/3 Saving fault metadata...")

fault_info = {
    'Cell': {'severity': 'High', 'icon': '⚡', 'loss': '5-15%', 'action': 'Inspect cell, check connections'},
    'Cell-Multi': {'severity': 'Critical', 'icon': '🔥', 'loss': '20-40%', 'action': 'Replace module immediately'},
    'Cracking': {'severity': 'Medium', 'icon': '💔', 'loss': '3-10%', 'action': 'Monitor and schedule replacement'},
    'Diode': {'severity': 'High', 'icon': '⚙️', 'loss': '10-25%', 'action': 'Replace bypass diode'},
    'Diode-Multi': {'severity': 'Critical', 'icon': '🚨', 'loss': '30-50%', 'action': 'Emergency diode replacement'},
    'Hot-Spot': {'severity': 'High', 'icon': '🔥', 'loss': '15-30%', 'action': 'Check for shading, replace if needed'},
    'Hot-Spot-Multi': {'severity': 'Critical', 'icon': '🚨', 'loss': '40-70%', 'action': 'URGENT: Disconnect and replace'},
    'No-Anomaly': {'severity': 'Low', 'icon': '✅', 'loss': '0%', 'action': 'Continue routine monitoring'},
    'Offline-Module': {'severity': 'Critical', 'icon': '⚠️', 'loss': '100%', 'action': 'Check connections, test output'},
    'Shadowing': {'severity': 'Medium', 'icon': '🌳', 'loss': '10-30%', 'action': 'Remove shading source'},
    'Soiling': {'severity': 'Low', 'icon': '🧹', 'loss': '2-8%', 'action': 'Clean panels'},
    'Vegetation': {'severity': 'Medium', 'icon': '🌱', 'loss': '5-20%', 'action': 'Remove vegetation'}
}

with open('models/fault_info.json', 'w') as f:
    json.dump(fault_info, f, indent=2)
print("   ✓ Fault metadata saved")

print("\n3/3 Saving model info...")

metadata = {
    'model_name': 'Solar Fault Detection YOLOv8n-cls',
    'version': '1.0.0',
    'created': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
    'architecture': 'YOLOv8n-cls',
    'accuracy': {'top1': 75.88, 'top5': 98.46},
    'classes': list(fault_info.keys()),
    'num_classes': 12,
    'image_size': 224,
    'training_images': 15996,
    'developer': 'Emmanuel Bilson',
    'institution': 'Ashesi University'
}

with open('models/model_metadata.json', 'w') as f:
    json.dump(metadata, f, indent=2)
print("   ✓ Model metadata saved")

print("\n" + "="*60)
full_path = os.path.abspath('models')
print(f"Files saved to: {full_path}")
print("\nPackaged files:")

for file in os.listdir('models'):
    filepath = f'models/{file}'
    size = os.path.getsize(filepath) / (1024*1024)
    print(f"   • {file} ({size:.2f} MB)")

print("\n" + "="*60)
print("✅ MODEL PACKAGING COMPLETE!")
print("\nModel files are in the 'models/' folder")
print("="*60)