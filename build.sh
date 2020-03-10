#!/bin/sh -x

AWS_DEFAULT_REGION=us-west-2
AWS_ACCOUNT_ID=9999999999999
IMAGE_REPO_NAME=kmsample
IMAGE_TAG=latest
aws --region $AWS_DEFAULT_REGION ecr get-login-password | docker login --password-stdin --username AWS $AWS_ACCOUNT_ID.dkr.ecr.$AWS_DEFAULT_REGION.amazonaws.com 
docker build -t $IMAGE_REPO_NAME:$IMAGE_TAG .
docker tag $IMAGE_REPO_NAME:$IMAGE_TAG $AWS_ACCOUNT_ID.dkr.ecr.$AWS_DEFAULT_REGION.amazonaws.com/$IMAGE_REPO_NAME:$IMAGE_TAG
docker push $AWS_ACCOUNT_ID.dkr.ecr.$AWS_DEFAULT_REGION.amazonaws.com/$IMAGE_REPO_NAME:$IMAGE_TAG
