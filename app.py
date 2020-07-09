#!/usr/bin/env python3

from aws_cdk import core

from ecs_cdk_sample.ecs_cdk_sample_stack import EcsCdkSampleStack


app = core.App()
EcsCdkSampleStack(app, "ecs-cdk-sample")

app.synth()
