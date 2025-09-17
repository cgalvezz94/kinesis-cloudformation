output "kinesis_stream_arn" {
  description = "ARN del stream de Kinesis"
  value       = aws_kinesis_stream.data_stream.arn
}

output "lambda_function_name" {
  description = "Nombre de la función Lambda"
  value       = aws_lambda_function.stream_processor.function_name
}

output "grafana_workspace_id" {
  description = "ID del workspace de Grafana"
  value       = aws_grafana_workspace.grafana.id
}

output "ecs_task_definition_arn" {
  description = "ARN de la definición de tarea ECS"
  value       = aws_ecs_task_definition.binance_task.arn
}