# AWS deployment plan — NOT YET DEPLOYED
1. Obtain explicit approval and set an AWS Budget and cost alert.
2. Confirm AWS CLI identity (`aws sts get-caller-identity`), region, IAM least-privilege, and data policy.
3. Build and smoke-test container locally: `docker build -t joule:dev .`; `docker run -p 8080:8080 joule:dev`; `curl http://localhost:8080/health`.
4. Create a private ECR repository and push the tested image.
5. Create ECS task definition (Fargate ARM64 on a supported region, or EC2 Graviton) using the ECR image, with logs to CloudWatch.
6. Keep initial service **private**; use an approved tunnel or restrict ingress/authentication before exposing an endpoint. The API as supplied has NO authentication, so do not expose it publicly.
7. Run authorized synthetic test images through POST /analyze on the AWS task; record actual runtime and CloudWatch logs.
8. Stop and remove resources after testing. Preserve cost and results evidence.

AWS official guide: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ECS_AWSCLI_Fargate.html
NOTE: AWS has not been deployed here; cloud credit and resource prices must be checked first.
