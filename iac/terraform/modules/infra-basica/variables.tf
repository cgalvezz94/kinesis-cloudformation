variable "bucket_name" {
  type        = string
  description = "Nombre base del bucket S3 para Lambdas"
  default     = "mi-bucket-lambdas"
}

variable "managed_policy_arns_lambda_role" {
  type        = set(string)
  description = "Lista de políticas gestionadas para el role"
  default     = [
    "arn:aws:iam::aws:policy/service-role/AWSLambdaKinesisExecutionRole",
    "arn:aws:iam::aws:policy/AmazonTimestreamFullAccess",
    "arn:aws:iam::aws:policy/CloudWatchLogsFullAccess"
  ]
}

variable "managed_policy_arns_grafana_role" {
  type        = set(string)
  description = "Lista de políticas gestionadas para el role"
  default     = [
    "arn:aws:iam::aws:policy/AWSGrafanaAccountAdministrator",
    "arn:aws:iam::aws:policy/CloudWatchLogsFullAccess",
    "arn:aws:iam::aws:policy/AWSXrayFullAccess",
    "arn:aws:iam::aws:policy/AmazonSNSFullAccess",
    "arn:aws:iam::aws:policy/AmazonDynamoDBFullAccess"
  ]
}

variable "managed_policy_arns_ecs_role" {
  type        = set(string)
  description = "Lista de políticas gestionadas para el role"
  default     = [
    "arn:aws:iam::aws:policy/service-role/AmazonECSTaskExecutionRolePolicy"
  ]
}