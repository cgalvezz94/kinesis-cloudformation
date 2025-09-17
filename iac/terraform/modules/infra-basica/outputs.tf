output "lambda_role_arn" {
  description = "ARN del role de Lambda"
  value       = aws_iam_role.lambda_role.arn
}

output "lambda_s3_bucket_name" {
  value = aws_s3_bucket.lambda_bucket.id
}

output "grafana_role_arn" {
  description = "ARN del role de Grafana"
  value       = aws_iam_role.grafana_role.arn
}

output "binance_cluster_name" {
  value = aws_ecs_cluster.binance_cluster.name
}

output "ecs_role_arn" {
  description = "ARN del role de ECS"
  value       = aws_iam_role.ecs_role.arn
}

output "binance_log_group_name" {
  description = "Nombre del grupo de logs"
  value       = aws_cloudwatch_log_group.binance_log_group.name
}