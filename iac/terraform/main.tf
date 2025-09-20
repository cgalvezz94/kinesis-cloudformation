terraform {
  required_version = ">= 1.5.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.30.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
}


module "infra-basica" {
  source = "./modules/infra-basica"
  bucket_name   = "mi-bucket-lambdas-binance"
}

module "infra-redes" {
  source = "./modules/infra-redes"
}

module "infra-secundaria" {
  source = "./modules/infra-secundaria"
  lambda_role_arn       = module.infra-basica.lambda_role_arn
  ecs_task_role_arn     = module.infra-basica.ecs_role_arn
  grafana_role_arn      = module.infra-basica.grafana_role_arn
  lambda_s3_bucket      = module.infra-basica.lambda_s3_bucket_name
  log_group_name        = module.infra-basica.binance_log_group_name
  stream_name           = "binance-trades"
  stream_mode           = "ON_DEMAND"
  retention_hours       = 24
  project_name          = "kinesis-project"
}