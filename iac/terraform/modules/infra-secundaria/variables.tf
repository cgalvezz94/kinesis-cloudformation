variable "stream_name" {
  type        = string
  default     = "binance-trades-v3"
  description = "Nombre del stream de Kinesis"
}

variable "stream_mode" {
  type        = string
  default     = "ON_DEMAND"
  description = "Modo del stream"
  validation {
    condition     = contains(["PROVISIONED", "ON_DEMAND"], var.stream_mode)
    error_message = "stream_mode debe ser PROVISIONED o ON_DEMAND"
  }
}

variable "retention_hours" {
  type        = number
  default     = 24
  description = "Periodo de retención en horas"
}

variable "project_name" {
  type        = string
  default     = "kinesis-project"
  description = "Nombre del proyecto"
}

variable "lambda_role_arn" {
  type        = string
  description = "ARN del rol de ejecución de Lambda"
}

variable "lambda_s3_bucket" {
  type        = string
  description = "Nombre del bucket S3 con el código Lambda"
}

variable "grafana_role_arn" {
  type        = string
  description = "ARN del rol de Grafana"
}

variable "ecs_task_role_arn" {
  type        = string
  description = "ARN del rol de ejecución de ECS"
}

variable "log_group_name" {
  type        = string
  description = "Nombre del grupo de logs para ECS"
}