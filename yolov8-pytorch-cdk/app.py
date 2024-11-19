#!/usr/bin/env python3
import os
import aws_cdk as cdk
from cdk.yolov8_sagemaker import YOLOv10SageMakerStack

app = cdk.App()
YOLOv10SageMakerStack(app, "YOLOv10SageMakerStack",)

app.synth()